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

#include "sql.h"
#include "crawl.h"

int main()
{
	std::cout << test(1, 2) << std::endl;
	std::cout << test2(1, 2) << std::endl;

	return 0;
}
