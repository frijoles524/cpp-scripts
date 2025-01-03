all:
	g++ -o math math.cpp
	cd ctof && make

check:
	python3 tests.py

clean:
	rm math
	cd ctof && make clean
