// ConsoleApplication1.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <cassert>
#include <string>

using namespace std;

enum StateName{
	STATE_INP, STATE_OUT, STATE_EVEN, STATE_ODD
};

enum Signature {
	SIG_INP, SIG_ODD, SIG_EVEN, SIG_OUT
};

struct stateMachine{
	StateName stateName;
	int signature;
	int difference; //xor result of this state's signature and next state's signature
	stateMachine* nextState;
};

int global;
int G = SIG_INP;
string output;

stateMachine inp = {STATE_INP,
					SIG_INP,
					SIG_INP ^ SIG_OUT};

stateMachine odd = {STATE_ODD,
					SIG_ODD,
					SIG_ODD ^ SIG_INP};

stateMachine even = {STATE_EVEN,
					SIG_EVEN,
					SIG_EVEN ^ SIG_INP};

stateMachine out = {STATE_OUT,
					SIG_OUT,
					SIG_OUT ^ SIG_EVEN};

void driveState(stateMachine& state){

	switch(state.stateName){
		case(STATE_INP) :
			cin >> global;
			if(global % 2) {
				state.nextState = &odd;
				G = G ^ state.nextState->difference;
			}
			else {
				state.nextState = &even;
				G = G ^ state.nextState->difference;
			}
			break;

		case(STATE_OUT) :
			cout << output << endl;
			state.nextState = &inp;
			G = G ^ state.nextState->difference;
			break;

		case(STATE_EVEN) :
			output = "EVEN";
			state.nextState = &out;
			G = (G ^ state.nextState->difference) ^ (0); //fan-in : xor'ed with extra difference variable
			break;

		case(STATE_ODD) :
			output = "ODD";
			state.nextState = &out;
			G = (G ^ state.nextState->difference) ^ (even.signature ^ odd.signature); //fan-in : xor'ed with extra difference variable
			break;

	}

	assert(G == state.nextState->signature);
	
}


int main(int argc, char* argv[])
{
	stateMachine state = inp;


	while(1){
		driveState(state);
		state = *(state.nextState);
	}

	return 0;
}

