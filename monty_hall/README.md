## Monty Hall

# Monty Hall Problem Solution using Monte Carlo Method

## Introduction

The Monty Hall problem is a famous probability puzzle based on a game show scenario. The problem is named after Monty Hall, the original host of the game show "Let's Make a Deal". The basic premise is as follows:

1. A contestant is presented with three doors. Behind one door is a car (the prize), and behind the other two doors are goats.
2. The contestant picks one of the three doors.
3. The host, who knows what is behind each door, opens one of the remaining two doors to reveal a goat.
4. The contestant is then given the choice to either stick with their original pick or switch to the other remaining door.

The question is: Should the contestant stick with their initial choice or switch doors to maximize their chances of winning the car?

Intuitively, it might seem like it doesn't matter, as there are two doors left and thus a 50/50 chance. However, probability theory shows that switching doors actually gives the contestant a 2/3 chance of winning, while sticking with the original choice gives a 1/3 chance of winning.

## Monte Carlo Method

The Monte Carlo method is a statistical technique that allows for the numerical estimation of complex problems. It relies on random sampling and repeated simulations to obtain results. In this context, we use the Monte Carlo method to simulate the Monty Hall game multiple times and observe the outcomes.

## Code Overview

This code simulates the Monty Hall problem using the Monte Carlo method. It repeatedly plays the game with a large number of iterations to empirically determine the probabilities of winning by switching and by sticking with the original choice.

## Inspiration

The book The Drunkard's Walk: How Randomness Rules Our Lives 
ISBN-10 9780307377548
ISBN-13 978-0375424045


ChatGPT was used to compose this text 😄