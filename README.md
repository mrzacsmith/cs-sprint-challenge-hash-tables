# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions =>
   `Hash(key) -> index` `{ "key" : "Zac", "value" : "phone #" }`
   `Array that uses the index to store the ke:value pair, and it associated the index to the key`
2. Collision resolution =>
   `each slot can hold a reference to a collection or chain of items. A linked list can be used to chain a list of collisions, so once we have the key, then can do a quick search of the chains in the same index. Open addressing is when a index is filled, it will be moved to the right until a opening is found.`
3. Performance of basic hash table operations =>
   `Taking collisions into account, worst case: search, insertation and deletation operations are linear 0(n) and not constant. Average case is constabt 0(1) if handle collisions well and do an excellent job of spreading data evenly across the hash table.`
4. Load factor =>
   `(number of items) / (total number of slots) and should resize hash table when load factor is approx 0.7. Typically double the size of the hash table. Resizing is constant time o(1)`
5. Automatic resizing =>
   `when the hash table length is automatically resized when the load factor reaches a certain ratio.`
6. Various use cases for hash tables =>  
   `Storing anything where order does not matter, but speed of access does. Anything that has a key:value pairing, or that does not use a integer as a unique identifier. Also compilers, caching, password authenticaiton`

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [x] Create a forked copy of this project
- [x] Add your team lead as a collaborator on Github
- [x] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [x] Create a new branch: git checkout -b `<firstName-lastName>`.
- [x] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [x] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [x] Navigate into each exercise's directory
- [x] Read the instructions for the exercise in the README
- [x] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

_Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)_

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
