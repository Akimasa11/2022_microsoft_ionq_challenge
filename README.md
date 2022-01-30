# Welcome to quantum Valentine’s Day dating!

A fun adventure through the very first quantum Valentine’s Day dating game.

    ::::          ::::::      ::::      ::::    :::::::::
    ::::        ::::  ::::    ::::      ::::    :::::::::
    ::::       ::::    ::::   ::::      ::::    ::::
    ::::       ::::    ::::    ::::    ::::     ::::::::
    ::::       ::::    ::::     ::::  ::::      ::::
    ::::       ::::    ::::      ::::::::       ::::
    ::::::::::  ::::  ::::        ::::::        :::::::::
    ::::::::::    ::::::           ::::         :::::::::

## Team InterQonnected

Akimasa Ihara, Tyler King, Andy Schang, Anish Shanbhag

## What is it?

There are only 8 days left until Valentine’s Day and you have no date. Can you muster up the courage and charisma to win over your crush’s heart before it’s too late, or will you end up without a date for this special Quantum Valentine’s Day?! This fun little adventure combines the likes of dating and gaming with the help of classical and quantum computers. The player will go through a series of steps to test their wits about quantum computers and, depending on how knowledgeable the player is, they may either end up with a date, or get harshly rejected for Valentine's Day! So if you trust yourself to make the right moves to connect with your crush in just the right way, read the rules to the game and see if you can succeed!

## Rules

- The dating simulator starts with a 2-qubit system in a random state.
- The goal is to manipulate the system in order to get to some target state vector.
- Each turn, you can apply a quantum unitary gate (Pauli, Hadamard, SWAP, CNOT) to try to get your 2 qubit state closer to the target state.
- Once you achieve the target state vector, the game ends.
- Getting closer to the target state vector builds your budding relationship :D while moving away shifts you apart. D:
- Since there are only 8 days left and you need to get your date before Valentine’s Day, there will be a total of 7 turns to connect with your crush (one per day). If the target state vector is never achieved, the relationship falls through and you end up lonely :(.
- The final turn executes the circuit in a real quantum computer with 1024 shots and checks how many times the outcome state matches the target statevector (win - 80% success rate). If the counts are within the threshold, you win, otherwise you lose! 

## Quantum Aspect

Each turn the player will be adding gates to their real quantum circuit. As each turn passes, we use the ionq quantum simulator to simulate the current (idealized) state vector of the system according to the gates that have been added. In the final turn, the entire circuit will be sent to the real ionq quantum computer. After the job has been executed, our program will check to see if the final state is the correct target state (within a threshold of course due to noise).

## Details about Implementation

- All input operations by the user will occur through a command prompt in jupyter notebook
- When selecting a gate on a specific qubit, please state the gate and then the target qubit (either 1 or 2)
  - Acceptable examples for hadamard gate: "h1", "H2", "H 1", "Hadamard 1"
  - Note: this means that "cx1" means a CNot gate with the first qubit as the target and the second as the control
  - The gate and qubit closest to the string argument will be used
- SWAP gates do not need to have a specific qubit listed and CNOT gates should have the target qubit as their listed number

## Machine Learning Model

The game also has a versus mode in which you can compete against another secret admirer of your crush. Get to the target vector before they do, or you'll lose out on the golden opportunity to ask your crush out!  
***Note: the machine learning challenge mode is only able to work on local files at the moment.***

The opponent is powered by a machine learning model which has been trained to play the game the same way a player would. We used the deep Q reinforcement learning algorithm to train the neural network model, which means that we just let our model play games by itself over and over until it learned the best strategies. After only around an hour of training (about 40,000 training games), the opponent takes only 5 gates to finish the game. Do you have what it takes to win your crush over before a machine in disguise does?!?

## Our team's personal experience
Our team had a fun experience by connecting with peers of similar interest from accross the globe. We greatly enjoyed learning about each other and working as a group to develop our first ever quantum game as a team. We all appreciated the opportunity of being able to interact directly with experts and mentors at the forefront of the quantum computing industry and academia. We think we have grown both as individuals and as a team, and we are all looking forward to more quantum team challenges in the future. 

## Date

January 29th, 2022
