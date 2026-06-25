# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| "New Game" Button, after a win | Start a new game | Can't go on to the next game | Stuck on "You already won. Start a new game to play again." |
| 80 | "GO HIGHER" | "GO LOWER" | The hints were backwards |
| "New Game" Button, after a loss | Start a new game | Can't go on to the next game | Stuck on "Game over. Start a new game to try again." |
| 50 | See 50 in the History | 50 did not show up in the history | History is not updating properly |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


For this project I used Claude Sonnet. When I described the issues I was running into, claude was very good at finding where the issue originated from and proposed fixes that made sense. Although most suggestions were good, when I asked Claude to write the Demo section of the reflection.md file, it made logical errors that I had to manually correct.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

After refractoring the code with claude's help, I refreshed streamlit and tested each refractor by hand. After seeing that the logic was correct, I moved on to the next issue. I then asked claude to create pytests for each one of the refractored functions to make sure things were working as expected.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit's state is dependent on streamlit running without stopping. If streamlit is restarted, everything in the previous session is erased. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will reuse in future projects is making a commit after every refractor. One thing I would do differently next time is to trust AI less, seeing that a lot of the time it can make small logical errors.

I was scared that AI would do all the work for me, but now I see that it is not perfect and it requires a lot of overseeing. I learned that AI can speed up my understanding the program as a whole and also individual functions, but any changes should be reviewed before accepting them. 
