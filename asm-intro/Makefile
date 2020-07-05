CC=g++
FLAGS=-std=c++11
TARGET=main

all: $(TARGET)

func.o: func.S
	$(CC) -o $@ -c $^ 

main.o: main.cc
	$(CC) -o $@ -c $^
	
main: func.o main.o
	$(CC) -o $@ $^

.PHONY:
	clean

clean:
	rm -rf *.o $(TARGET)
