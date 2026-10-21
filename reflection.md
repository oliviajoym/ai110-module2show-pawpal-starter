# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- User should be able to:
    - add a pet and type of pet
    - schedule different tasks
    - see the generated schedule for the day

- Classes
    - Owner - responsible for the pet
    - Pet - holds pet name, species, and their owner, responsible for tasks
    - Task - holds a decription, a time constraint, and wheter the task repeats, responsible for completion
    - Scheduler - holds lists of scheduled tasks 

**b. Design changes**

- One change I made was the boolean repeated. It was good to show that task coud repeat but it was better to use an interval or frequency to show when it repeats.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
