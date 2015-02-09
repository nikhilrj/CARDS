// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

struct stateMachine{
	bool inBool;
	bool outBool;
	bool isEven;
	//stateMachine();
	int signature;
	stateMachine* nextState;
};

int global;
stateMachine inp = {1, 0, 0, 1};
stateMachine odd = {0, 0, 0, 2};
stateMachine even = {0, 0, 1, 3};
stateMachine out = {0, 1, 0, 4};

void driveState(stateMachine& state){
	//G = G xor d1

	if(state.inBool){
		cin >> global;
		if(global % 2){
			state.nextState = &odd;
		}
		else
			state.nextState = &even;
			
	}
	else if(state.outBool){
		cout << global << endl;
		state.nextState = &inp;
	}
	else if(state.isEven){
		global = 99;
		state.nextState = &out;
	}
	else{
		global = -1;
		state.nextState = &out;
	}

	//ASSERT G == s1
	
}


int _tmain(int argc, _TCHAR* argv[])
{
	stateMachine state = inp;


	while(1){
		driveState(state);
		state = *(state.nextState);
	}

	return 0;
}

