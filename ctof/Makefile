all:
	g++ -o libctof.so -fpic -shared libctof.cpp
	g++ -c ctof.cpp -o ctof.o -I.
	g++ -o ctof ctof.o -lctof -L.
	echo "compilation done. make sure to run the program with LD_LIBRARY_PATH=. prepended unless you know how or are willing to install the library"

clean:
	rm ctof.o
	rm libctof.so
	rm ctof
