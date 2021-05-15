############################################################
CXX = g++
CXXFLAGS = -g -Wall -Wextra -pedantic -lcurl -lboost_filesystem -lboost_system -std=c++17 -I $(HEADERINCLUDE)
EXC = build
OBJ = obj
HEADERINCLUDE = /home/itsme/Desktop/git_repos/tiss-crawler/include
############################################################

OUTPUT_NAME = tiss_crawl

all: $(OBJ)/main.o $(OBJ)/sql.o $(OBJ)/crawl.o
	$(CXX) $(CXXFLAGS) -o $(EXC)/$(OUTPUT_NAME) $(OBJ)/main.o $(OBJ)/sql.o $(OBJ)/crawl.o

$(OBJ)/main.o: src/main.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c src/main.cpp

$(OBJ)/crawl.o: src/crawl.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c src/crawl.cpp

$(OBJ)/sql.o: src/sql.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c src/sql.cpp

clean:
	$(RM) $(OBJ)/main.o $(OBJ)/sql.o $(OBJ)/crawl.o

run: $(EXC)/$(OUTPUT_NAME)
	./$(EXC)/$(OUTPUT_NAME)
