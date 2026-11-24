
# AI coding workflow

From https://ai.engineer/talks/-QFHIoCo-Ko-ai-coding-workflow

## What I understood of the process:

- he uses a skill "grill-me" to agree on the functional requirements. This skill asked him questions to they could come up with a prd.md document which summarize the requirements. There are user-stories in the document. He does not read the prd.md because it will just check that the LLM made a good summary of the agreement. The agreement is the destination
- he asked to make Kanban task, with each having blocking task, isAFK property. Multiple user-stories can be implemented by one task. However, the LLM comes often with horizontally-implemented task (i.e.  change DB -> change BE -> change FE). This is not going to work because there is no testing which act like feedback loop to AI. Therefore, he reads this phase result and iterates until we get to vertical tasks
- He then lets the agents work on the Kanban task. Some task can be done in parallel. He speaks of Test-Driven-Development, to let the AI test that the code is correct. I guess he wrote the integrated test in advance. it means that it is important that the code base is easy to test. Having module test is important. The important part is now to design the modules, writes the test which works only on the interface, and let AI write the implementation. The human role is now to know the modules and their responsibilities, but not reviewing the implementation as long as the module tests pass.

## Interesting point:

- writing bad code will make bad LLM decision in the future (garbage in, garbage out)
- There is a dumb zone if the discussion has been too long with the LLM. We can clear by making a new discussion, or compact the discussion. I have to tell that I do not understand why statement is true.
- If we want to work cross-layer, developer needs to know the layers. FE versus BE is not a thing anymore
- putting the prd.md in the repo is a bad idea because it might expired (i.e. functional requirements are not valid anymore) and influence the AI badly.
- making a skill that automatically reviews the code with OMP standards, and which is available to the AI implementing it.

## Questions:

- where is code review in this process? Do we still need it to be done by another human? I'm asking because reviewing code is not fun, and it is even less funny when you know that it was spit from an AI and that your colleague did not review it. On the other hand, I can spot some functional mistakes in today's AI-written PRs.
