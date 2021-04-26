#include <string>
#include <iostream>
#include <curl/curl.h>
#include <fstream>
#include <vector>
#include <cstring>
#include <boost/filesystem.hpp>
#include <filesystem>
#include <boost/crc.hpp>
#include <istream>
#include <chrono>
#include <ctime>
#include <cstdio>
#include <iomanip>

// function inserting the entries into the logfile
void insert_logfile(std::string path_to_logfile, std::string msg_log1, std::string msg_log2 = "")
{
	// open the (log) file to write into
	std::ofstream logfile_ofstream;
	logfile_ofstream.open(path_to_logfile+"_log"+".txt", std::ios_base::app);

	// get the time and date
	std::time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
	char temp_insert_date_logfile[100] = {0};
	std::strftime(temp_insert_date_logfile, sizeof(temp_insert_date_logfile), "%Y-%m-%d %X ", std::localtime(&now));

	logfile_ofstream << temp_insert_date_logfile;
	std::cout << temp_insert_date_logfile;

	unsigned int padLen = 40;	// whitespace padding of the string
	if (msg_log1.size() > padLen)	// prevent an error when the logmsg1 is longer than the set paddin length
	{
		padLen = msg_log1.size();
	}

	msg_log1.append(padLen - msg_log1.size(), ' ');

	logfile_ofstream << msg_log1;
	std::cout << msg_log1;

	if (msg_log2 != "")
	{
		logfile_ofstream << msg_log2 << std::endl;
		std::cout << msg_log2 << std::endl;
	}
	else
	{
		logfile_ofstream << std::endl;
		std::cout << std::endl;
	}
}

// datastream (fetched source files) used by fetch_source_single_page
size_t write_fetched_data(void* ptr, size_t size, size_t nmemb, void* data)
{
	std::string* result = static_cast<std::string*>(data);
	*result += std::string((char*)ptr, size* nmemb);
	return size* nmemb;
}

// fetch the source code of a single page
std::string fetch_source_single_page(std::string url_full)
{
	std::string useragent = "...";		// user agent string

	CURL* ch_ = curl_easy_init();				// create a CURL handle
	char error_buffer[CURL_ERROR_SIZE];
	std::cout << error_buffer << std::endl;		// display the error log

	// SET OPTIONS
	curl_easy_setopt(ch_, CURLOPT_ERRORBUFFER, error_buffer);			// option set for error_buffer
	curl_easy_setopt(ch_, CURLOPT_WRITEFUNCTION, &write_fetched_data);	// pointer to the recieved data

	std::string result;
	curl_easy_setopt(ch_, CURLOPT_WRITEDATA, &result);					// write the data into this variable

	int id = 1;
	curl_easy_setopt(ch_, CURLOPT_VERBOSE, id);							// 1 ... a lot of verbose informations
	curl_easy_setopt(ch_, CURLOPT_URL, url_full.c_str());
	curl_easy_setopt(ch_, CURLOPT_USERAGENT, useragent.c_str());		// set user agent string
	curl_easy_setopt(ch_, CURLOPT_CONNECTTIMEOUT, 10);					// time(seconds) we want to be connected to the server
	curl_easy_setopt(ch_, CURLOPT_TIMEOUT, 30);							// maximum time(seconds) the transfer of the files may need
	// SET OPTIONS

	curl_easy_perform(ch_);	// start transfer with the options set above (multiple calls of this for the same handle is possible)
	curl_easy_cleanup(ch_);	// purges the handle (when crawling is done)

	return result;
}


// filestream used by fetch_PDF_from_URL
size_t write_file_data(void* ptr, size_t size, size_t nmemb, FILE* stream)
{
	size_t written = fwrite(ptr, size, nmemb, stream);
	return written;
}


// download a PDF given by an URL
void fetch_PDF_from_URL(std::string fetch_pdf_url, std::string filename, std::string temp_files_path)
{
	CURL* curl;
	FILE* fp;
	std::string useragent = "...";		// user agent string

	// define locations where to save the file temporarily
	std::string outfilename = temp_files_path+filename;
	const char *cfilename = outfilename.c_str();

	curl = curl_easy_init();

	if (curl)
	{
		fp = fopen(cfilename, "wb");
		curl_easy_setopt(curl, CURLOPT_URL, fetch_pdf_url.c_str());
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_file_data);
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
		curl_easy_setopt(curl, CURLOPT_USERAGENT, useragent.c_str());		// set user agent string
		curl_easy_perform(curl);

		// cleanup
		curl_easy_cleanup(curl);
		fclose(fp);
	}
}


// cut the std::string / extract the filename which is the last part of the std::string
std::string filename_extraction(std::string process_string, std::string delimiter)
{
	size_t pos = 0;
	std::string token;

	while ((pos = process_string.find(delimiter)) != std::string::npos)
	{
		token = process_string.substr(0, pos);
		process_string.erase(0, pos + delimiter.length());	// remove the parts of the string left of the delimiter
	}

	return process_string;	// return the last part of the std::string (the filename)
}


// starting from the obtained page source code, this function extracts the links to the PDFs as well as the information about the PDFs. The obtained
// information is stored in the two std::vectors extracted_data1 and extracted_data2
void extract_PDF_URL_and_descriptions(std::string result, std::vector<std::string>& fetched_URLs, std::vector<std::string>& fetched_URLs_descriptions, std::string logpath)
{
	// iterate the std::string and find the desired elements
	for (unsigned int i = 0; i < result.length()-8; i++)
	{
		// rolling comparison to find open '<a href="' tags
		int ahref_compare = result.compare(i, 9, "<a href=\"");

		// extract the target URL to the PDF and the description according to the page source code
		if (ahref_compare == 0)	// found an opening '<a href="' tag
		{
			bool close_URL = false;
			i += 9;							// increment variable i by 9 to set the position at the end of the opening bracket
			int start_extract_pos_URL = i;	// cache the start position

			// extract the link to the PDF
			std::string extract_URL;		// stores the link to the PDF

			bool already_in_list = false;	// prevent the same PDF being pushed multiple times into the std::vec (which would cause problems with further file processing)

			while (close_URL == false)
			{
				i++;

				if (result[i] == '\"')	// end of URL reached
				{
					close_URL = true;
					extract_URL.append(result.begin()+start_extract_pos_URL, result.begin()+i);

					// check whether this entry is already in the std::vector (multiple links leading to the same PDF)
					for (unsigned int j = 0; j < fetched_URLs.size(); j++)
					{

						if (filename_extraction(fetched_URLs[j], "/") == filename_extraction(extract_URL, "/"))
						{
							already_in_list = true;
							break;
						}
					}

					// only add the information _if_ this element is not already in the list (else the PDF would be added multiple times
					if (already_in_list == false)
					{
						fetched_URLs.push_back(extract_URL);
					}
				}
				else if (i == result.length())	// error .. end of string while tag is open!
				{
					// TODO: just skip this element
					std::cout << "error parsing the source code (wrong syntax at closing tag for PDF-extration)" << std::endl;
					std::cout << "i = " << i << std::endl;
					exit(1);
				}
			}

			// increase i until '>' is reached (which marks the end of the URL and beginning of the description)
			while (result[i] != '>')
				i++;

			// get the description of the URL (as viewed by the browser)
			bool close_descr = false;
			i += 1;						// increment variable i by 9 to set the position at the end of the opening bracket
			int start_extract_pos_desc = i;	// cache the start position

			std::string extract_desc;	// description of the file

			while (close_descr == false)
			{
				i++;

				if (result[i] == '<')	// end of desc reached
				{
					close_descr = true;
					extract_desc.append(result.begin()+start_extract_pos_desc, result.begin()+i);

					// only add the information _if_ this element is not already in the list (else the PDF would be added multiple times
					if (already_in_list == false)
					{
						// clean-up the url (remove undesired strings)
						std::string delete_string_search = "&nbsp;";	// search and remove this string from the folder name
						std::string::size_type del_pos_search = extract_desc.find(delete_string_search);	// search the position of this string

						// string to delete has been found -> remove this part from the url (which is used as a folder name later on)
						if (del_pos_search != std::string::npos)	// if a position has been found it will be removed
						{
							insert_logfile(logpath, "cleanup extract_desc("+delete_string_search+"):", extract_desc);
							extract_desc.erase(del_pos_search, delete_string_search.length());
						}

						// push the description to the std::vector
						fetched_URLs_descriptions.push_back(extract_desc);
					}
				}
				else if (i == result.length())	// error .. end of string while tag is open!
				{
					// TODO: just skip this element
					std::cout << "error parsing the source code (wrong syntax of a closing tag for description-extration)" << std::endl;
					std::cout << "i = " << i << std::endl;
					exit(1);
				}
			}
		}
	}
}


// courtesy: Toby Speight (https://codereview.stackexchange.com/questions/133483/calculate-the-crc32-of-the-contents-of-a-file-using-boost)
// calculates the crc32 checksum for a given file
uint32_t crc32(std::string file_read_open)
{
	char buf[4096];
	boost::crc_32_type result;

	std::filebuf fb;

	if (fb.open (file_read_open, std::ios::in))
	{
		std::istream is(&fb);

		// calculate the crc32 checksum
		do
		{
			is.read(buf, sizeof buf);
			result.process_bytes(buf, is.gcount());
		}
		while (is);

		if (is.eof())
		{
			return result.checksum();
		}
		else
		{
			throw std::runtime_error("File read failed");
			return 0;
		}

		fb.close();
	}
	else
	{
		std::cout << "File read failed" << std::endl;
		return 0;
	}

	return 0;
}

int main()
{
	// the site one wants to crawl
	std::string TLD						= "https://www.tuwien.at";													// top-level-domain
	std::string page_to_crawl			= "/tu-wien/organisation/zentrale-bereiche/studienabteilung/studienplaene";	// the page which will be crawled

	// file paths
	std::string temp_files_path			= "temp_downloads/";	// location where the temp downloaded files are stored
	std::string curricula_files_path	= "curricula/";			// location where the downloaded curricula are stored
	std::string log_files_path			= "logs/";				// location where the logs (info about the crawl) are stored

	// define the names of the folders where the curricula are stored to (corresponds to the numbering elements in the search_str std::vector)
	std::vector<std::string> folder_name_structure{"Bachelor/", "Master/", "Doktor/", "Erweiterungsstudium/", "Gemeinsame Studienprogramme/", "Alte Studienpläne/"};

	// the elements by which the curricula are sorted into (according to these searchstrings)
	std::vector<std::string> search_str{"BSc", "MSc", "Doktor", "Erweiterungsstudium", "Gemeinsame_Studienprogramme", "Alte_Studienplaene"};

	// fetch the date of today to insert it into the filename (and the logfile name)
	std::time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
	char temp_insert_date[100]			= {0};
	char temp_insert_date_logfile[100]	= {0};
	std::strftime(temp_insert_date, sizeof(temp_insert_date), " (%Y-%m-%d %X)", std::localtime(&now));
	std::strftime(temp_insert_date_logfile, sizeof(temp_insert_date_logfile), "%Y-%m-%d %X", std::localtime(&now));

 	insert_logfile(log_files_path+temp_insert_date_logfile, "start");
 	insert_logfile(log_files_path+temp_insert_date_logfile, "TLD: ", TLD);
 	insert_logfile(log_files_path+temp_insert_date_logfile, "crawled site: ", page_to_crawl);
 	insert_logfile(log_files_path+temp_insert_date_logfile, "temp download folder: ", temp_files_path);
 	insert_logfile(log_files_path+temp_insert_date_logfile, "curricula folder: ", curricula_files_path);

	for (unsigned int i = 0; i < search_str.size(); i++)
	{
		insert_logfile(log_files_path+temp_insert_date_logfile, "searchstr: "+std::to_string(i), search_str[i]);
	}

	return 0;
}
