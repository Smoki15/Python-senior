const int row[8] = {
  13, 8, 17, 10, 5, 16, 4, 14
};

// 2-dimensional array of column pin numbers:
const int col[8] = {
  9, 3, 2, 12, 15, 11, 7, 6
};

// 2-dimensional array of pixels:
int pixels[8][8];

int count = 1000;

char str[] = "EDCBA";
int strLen = sizeof(str);
int ptrChar = 0;

typedef bool charMapType[8][8];

const charMapType charDummy = {
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0}
};

const charMapType charA = {
  {0, 0, 0, 1, 1, 0, 0, 0},
  {0, 0, 0, 1, 1, 0, 0, 0},
  {0, 0, 1, 0, 0, 1, 0, 0},
  {0, 0, 1, 0, 0, 1, 0, 0},
  {0, 1, 1, 1, 1, 1, 1, 0},
  {0, 1, 0, 0, 0, 0, 1, 0},
  {1, 1, 0, 0, 0, 0, 1, 1},
  {1, 0, 0, 0, 0, 0, 0, 1}
};

const charMapType charB = {
  {1, 1, 1, 1, 1, 1, 0, 0},
  {0, 1, 0, 0, 0, 0, 1, 0},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 1, 1, 1, 1, 1, 0},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 1, 0},
  {1, 1, 1, 1, 1, 1, 0, 0}
};

const charMapType charC = {
  {0, 1, 1, 1, 1, 1, 1, 0},
  {1, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0},
  {1, 0, 0, 0, 0, 0, 0, 0},
  {1, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 1},
  {0, 1, 1, 1, 1, 1, 1, 0}
};

const charMapType charD = {
  {1, 1, 1, 1, 1, 1, 1, 0},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {0, 1, 0, 0, 0, 0, 0, 1},
  {1, 1, 1, 1, 1, 1, 1, 0}
};

const charMapType charE = {
  {1, 1, 1, 1, 1, 1, 1, 1},
  {0, 1, 0, 0, 0, 0, 0, 0},
  {0, 1, 0, 0, 0, 0, 0, 0},
  {0, 1, 1, 1, 1, 1, 1, 0},
  {0, 1, 0, 0, 0, 0, 0, 0},
  {0, 1, 0, 0, 0, 0, 0, 0},
  {0, 1, 0, 0, 0, 0, 0, 0},
  {1, 1, 1, 1, 1, 1, 1, 1}
};

const charMapType *charMap[5] = { &charA, &charB, &charC, &charD, &charE };

void setup() {
	// initialize the I/O pins as outputs iterate over the pins:
	for (int thisPin = 0; thisPin < 8; thisPin++) {
		// initialize the output pins:
		pinMode(col[thisPin], OUTPUT);
		pinMode(row[thisPin], OUTPUT);
		// take the col pins (i.e. the cathodes) high to ensure that the LEDS are off:
		digitalWrite(col[thisPin], HIGH);
	}

	// initialize the pixel matrix:
	/*for (int x = 0; x < 8; x++) {
		for (int y = 0; y < 8; y++) {
			pixels[x][y] = HIGH;
		}
	}*/

	setupChar();
}

void loop() {
	// draw the screen:
	refreshScreen();

	if (count-- == 0) {
		count = 1000;
		setupChar();
	}
}

void refreshScreen() {
	// iterate over the rows (anodes):
	for (int thisRow = 0; thisRow < 8; thisRow++) {
		// take the row pin (anode) high:
		digitalWrite(row[thisRow], HIGH);
		// iterate over the cols (cathodes):
		for (int thisCol = 0; thisCol < 8; thisCol++) {
			// get the state of the current pixel;
			int thisPixel = pixels[thisRow][thisCol];
			// when the row is HIGH and the col is LOW,
			// the LED where they meet turns on:
			digitalWrite(col[thisCol], thisPixel);
			// turn the pixel off:
			if (thisPixel == LOW) {
				digitalWrite(col[thisCol], HIGH);
			}
		}
		// take the row pin low to turn off the whole row:
		digitalWrite(row[thisRow], LOW);
	}
}

void setupChar() {
	char c = str[ptrChar];
	int offset = c - 'A';

	const charMapType *cMap = charMap[offset];
	//charMapType *cMap = &charDummy;

	for (int x = 0; x < 8; x++) {
		for (int y = 0; y < 8; y++) {
			bool v = (*cMap)[x][y];

			if (v) {
				pixels[x][y] = LOW;
			}
			else {
				pixels[x][y] = HIGH;
			}
		}
	}

	ptrChar++;
	if (ptrChar >= strLen - 1) {
		ptrChar = 0;
	}
}