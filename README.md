# Creating cytokine and peptide hormone-releasal metabolic tasks

This document provides the infortation required to succesfully pursue the MSP project and therefore should be read carefully. 
Following this document will hopefully ensure that you can deliver high quality research
that you can look back upon fondly and show others as part of your academic portfolio.

---
### Table of contents

- [Requirements](#project-requirements)
  - [Git usage](#git-usage) (see [Setting up & using Git](#setting-up-&-using-git) as
    well)
  - [Documentation](#documentation-procedure)
  - [Quality assessment](#quality-assessment-procedure)
- [Setting up & using Git](#setting-up-&-using-git)
  - [Setting up Git](#setting-up-git)
    - [Installing Git](#installing-git)
    - [Cloning repository](#cloning-git-repository)
  - [How to use Git](#using-git)
    - [Git bash](#git-bash)
    - [Github Desktop](#github-desktop)
- [Choosing a task/project management](#project-management)
  - [First assessor](#first-assessor)
    - [Becoming first assessor](#becoming-first-assessor)
    - [Ready for review](#ready-for-review)
    - [Additional changes](#additional-changes)
    - [Signing off](#signing-off)
  - [Second assessor](#second-assessor)
    - [Being called for review](#Called-for-review)
    - [Providing assessment](#Providing-assessent)
    - [Checking changes](#checking-changes)
    - [Signing off as second assessor](#signing-off-as-second-assessor)
- [Example Case](#example-case)
  - [Taking the task](#taking-the-case)
  - [Finding appropriate literature](#finding-appropriate-literature)
  - [Documenting the evidence](#documenting-the-evidence)
  - [Calling for review](#calling-for-review)
  - [Performing review assessment](#performing-review-assessment)
  - [Making changes](#making-changes)
  - [Assessing the changes](#assessing-the-changes)
  - [Signing off the task](#signing-off-the-task)
- [Report/presentation](#report-presentation)
  - [Report](#report)
    - [What should it include](#what-should-the-report-include)
    - [Writing tips](#writing-tips)
    - [Feedback](#report-feedback)
  - [Presentation](#presentation)
    - [Organising the presentation](#organising-the-presentation)
    - [Presentation tips](#presentation-tips)
- [Problems](#problems)

---

## Project requirements

Please adhere to the following manegerial requirements to make the project work
smoothly, speedily, and hopefully without problems:


### Git usage

All group members must create a github account and install git or Github Desktop and 
become collaborators to this repository. **All changes you make during the day
should be committed and pushed to the repository!** This will ensure both a paper-trail 
of your contributions and allows your research to remain easily identifyable; increasing 
the usefulness of the work you will do. See [Setting up & using Git](#setting-up-&-using-git) 
for a tutorial on how to do this.

### Documentation procedure

Any evidence identified from literature/schematic pictures, should be documented
**verbatum**: this means that for the documentation on the Github per
cytokine/hormone, you provide the sources, and literal text or pictures to
support your case. Of course in the report you must reference + summarize in your
own words (the reason for literal text is that checking and verifying the validity
of any cytokine- and hormone-tasks will be easier when I can read the text,
instead of searching within an article, with the added negative that in such a
case you might interpret literature differently from me and your peers). See
[Example Case](#example-case) for an example of how to approach this, as well as how to
formulate the actual ouput.

### Quality assessment procedure

While I think these tasks can be tackled individually, it is up to you whether you
want to do so or go after these task in larger groups, all evidence must be
reviewed by at least a second assessor that was not involved in the original task
construction (by the first assessor(s)).  Second/third assessor will be working on
their own tasks and thus some waiting time can be expected. 
During review by the second assessor, the first assessor(s) can start with an
additional task. Similarly if a third assessor is necessary or my own input is 
required, both assessors will move on to another task and pick up their original 
task when reviewed/assessed. See [Choosing a task/project management](#project-management) 
for how to indicate your involvement and sign-off. Make sure that in your commit 
messages for changes to git, if working in a group, you indicate all contributors' 
names (even if they did not commit/push anything themselves).
Assessment is based on the provided literature (and potentially some extra
googling, but they should be able to identify all information from the references
and verbatum documentation provided). They will then provide their assessment of
the following criteria:
- Correctness
  - Correct (they come to the same conclusions)
  - Unclear (different conclusions but original does not seem incorrect)
  - Full disagreement (the "first assessor(s)" missed something or made a mistake)

In case everything is correct, no other actions have to be taken and both first
and second assessor can continue with another task. When there is disagreement
but no obvious correct answer, the first and second assessors will attempt a
second search. If such a search does not yield new results/insights, they will
attempt to clarify the contradicting points and ask a third assessor to indicate
whether the problems are clearly defined. If this is the case, contact me
(Jelle.bonthuis@maastrichtuniversity.nl, or come by my office), indicating the
Github page with the evidence and all assessors can move on to another task
during my review. If my review indicates more work needs to be done, the first
assessors are responsible, and the second assessor will come in once again when
they are done.
In the unlikely case (hopefully) that the evidence seems to be completely wrong
(not the correct genes, entirely misinterpretted, different organisms etc), the
second assessor is responsible for providing in-depth commentary on what needs
to be changed, and the first assessor(s) will take this to continue and improve
their work.
- Documentation: 
  - Fully documented and clearly/logically summarised (including table of
        reactions, genes involved, and numbers refering to the verbatum text from
        literature somewhere else in the document).
  - Fully documented but difficult to navigate all relevant information
  - Not all information was present, or logical leaps in how one piece of
          evidence leads to another
  - Mostly or entirely lacking 

In case everything is fully documented and logically structured, no changes are
necessary. If fully documented but too much irrelevant inforomation is present,
or overall structure is difficult to disentangle, the second assessor provides
tips and high priority changes that are necessary in order for the documentation
to be useful for people not in the project - high priority is key; this does not
need to become an academic paper, it should be formatted/changes up to the point
that in a year, I can browse/peruse the results and easily find anything I need.
In case not all information was present, or some evidence appears to be missing,
this should be clearly communicated to the first assessors, and changed (as this
can easily lead to incorrect results or wrong interpretations).
In the unfortunate case of almost no documentation, refer to the
[Example Case](#example-case), provide written feedback to first assessors 
to help them on their way to fully document whatever is necessary.

---

## Setting up and using Git
Git is the most-used type of version control (the ability to see previous versions, and
to "go back" to them without necessarily losing other progress). Especially in
programming/software projects where multiple people work together and might all edit
similar code/files, this became crucial. See this (somewhat not-serious video) that
explains how useful this was: 

[![Video](https://i3.ytimg.com/vi/iaEnUXtiGsE/maxresdefault.jpg)](https://www.youtube.com/watch?v=iaEnUXtiGsE)

### Create a Github account 

- Follow the instructions [here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
(I recommend using your personal email, as your university email will eventually 
become inaccessible).
- Become collaborator 

### Installing Git

If you are a Linux user, I assume you can follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 

#### Windows

Installing Git on Windows is straightforward: 
 - Download the latest version of *Git for Windows* [here](https://gitforwindows.org)
 - Follow the installer instructions, and if given the option, choose to use Git Bash instead of the standard Git Windows Command Prompt.
 - After installation is complete, verify that it is working by opening Git Bash and typing `git --version`; you should see `git version 2.45.1.windows.1` or something similar.

 (Optionally) If you rather use a GUI instead of having to use the command line, you can
 install Github Desktop - *in addition to Git, **not** as a substitute*; do note that
 while this is easier 95% of the time you might run into an issue and will require Git 
 Bash, and learning the few Git commands you need won't hurt you (and is valuable 
 in many settings).
 - https://desktop.github.com/download/
 - Follow the setup instructions
 - Login to your Github 

#### Mac 


### Setting it up

Once you have it all installed, it is time to down


### How to use Git

The way of using Git (regarldless of whether you are using Github Desktop, or Git from
command-line interfaces) is to "fetch" (find new changes), "pull" (copy those changes to
your own device), and then after you make changes, you "push" (add changes the central
directory). In this manner, everyone has a central repository, but can make changes
independelty. When you and someone else make changes to the same file, you will be asked
to make a concious decision on how to "merge" those changes. In addition there will be a
complete history of all changes you all make to each file.

### Git Bash

 - At the start of the day, 

### Using git daily

 - At the start of the day, 



## Example Case

### Taking the task
<img width="975" height="609" alt="image" src="https://github.com/user-attachments/assets/345a038d-9718-421e-9fa2-dca696d5d783" />

   On the following [spreadsheet](https://docs.google.com/spreadsheets/d/1_SG6BUYSQPkR_8MzOA8YLUAw2p9PgF1CSNdOy6dspm4/edit?usp=sharing) we can find the tasks, and their status.
    First you check the list and find a peptide hormone or cytokine that you 
    interested in. A task has a status and it should not be taken by anyone. Select that
    you are working by writing "First assessment (inital, lastname" in the Active/Stage
    column. Put your name (or names in case you are doing this as a group), in the
    "First assessor" column. 
<img width="478" height="92" alt="image" src="https://github.com/user-attachments/assets/c33213b9-b311-42c4-8a3f-f62edb6391bb" />
<img width="487" height="123" alt="image" src="https://github.com/user-attachments/assets/85232abd-9418-4494-85bb-be47bb6812d4" />
    
   Now create a folder on your computer, in your *cloned* and *pulled* git directory, in the Tasks folder,
    here we will work on Task 701, insulin synthesis, so inside Tasks I added
    "Task_701_insulin_synthesis". I fill it with copies of the three files in the
    "Current_files" folder (remember to copy, not remove)! We then create two Word (or
    other text-related files), the main literature file: Insulin_synthesis_task_701.docx
    & the shortened notes file: Short_notes_Task_701_insulin_synthesis.docx. As the main
    literature file can become quite large (as you will see), the short notes file
    is there to write down any of the most important things to consider (such as some
    things we aren't very sure about, or that should maybe in the future be further
    explored).
<img width="975" height="190" alt="image" src="https://github.com/user-attachments/assets/d5a3c5c7-20ef-4277-adb8-766dcbcb9373" />
<img width="975" height="112" alt="image" src="https://github.com/user-attachments/assets/2510f15a-42ce-4f49-ac7c-1581543167cd" />


### Finding appropriate literature
   Now we need go about finding appropriate literature, which starts with finding the
     gene of the actual pre-pro-insulin; subsequently it's time to start reading some
      articles on the biosynthesis and processing. At this stage it is reccomended to
      read/skim a few different (review) articles to get a bit of an overview (one might go
      into more detail than others). Another important thing to not forget is looking up
      pictures on google images: often schematic overviews provide additional information
      which we can then later on look into. Be mindful of any mentions of genes and
      processes involved, as we will need to collate them in their entirety.
      
   Please see the case report I prepared in Task_701_insulin_synthesis, go through it
      carefully. I wrote it not entirely as I would like to see it from you, some of the
      order and overall flow is not in logical order for someone else to read in the
      future. However this is the order by which I found things, and hope to show how I
      often missed things which when reading/looking up other articles then came to
      light.

  There are some points that aren't inside the document itself (but please first read the insulin case document and short_notes, as otherwise this might be a little vague) which are described here:
  inside the metabolites_additions file we need add the following parts.
  <img width="975" height="259" alt="image" src="https://github.com/user-attachments/assets/d6aa5789-694e-48f9-b042-9d8058a654ce" />
1.	Gene-pseudo-metabolites are our stand in metabolites for genes, and thus have an AA sequence, and uniport/ensemble IDs
https://www.uniprot.org/uniprotkb/P01308/entry
<img width="975" height="284" alt="image" src="https://github.com/user-attachments/assets/6f8bf3cb-5bd2-403d-845d-83af75113aa2" />

2.	Because the signal peptide is cleaved from insulin, we take that sequence ; EDIT: in the actual file I called it ins-signal-peptide, as other peptides create other/different signal peptides!
3.	ERO1-4SH is an enzyme metabolite that is taking up and giving protons, however since this is a protein complex and overall AA sequences and actual atoms don’t match, we therefore leave it empty in the metabolite formula department
<img width="975" height="307" alt="image" src="https://github.com/user-attachments/assets/dc304269-04bc-4ee7-8d71-48e67cc3f211" />
Insulin and C-peptide themselves have sequences we derived from the original sequence, note that this article indicates that CPE cut off two AA’s and so these are not in the final insulin (the two arginine (R) at position 56)
<img width="975" height="586" alt="image" src="https://github.com/user-attachments/assets/c5025ac0-87de-4e67-9bc4-7c2cd2c0b721" />
Finishing it up:
<img width="975" height="334" alt="image" src="https://github.com/user-attachments/assets/8e636d64-1bc6-46fb-b526-263e7915943d" />
This way, if I ever decide on adding in the metabolite formulas for these other parts, I can easily find them by their type (mentioned in project_notes), if one would have to add anything else, just put a ; 
so something like gene-pseudo-metabolite ; “other message”.
Note that if there’s a metabolite such as ATP or water (or anything else that is actually a metabolite and not a peptide), try finding the SMILES on pubchem (and put it in metabolite formula), see this example of ATP: 
https://pubchem.ncbi.nlm.nih.gov/compound/5957 
<img width="975" height="138" alt="image" src="https://github.com/user-attachments/assets/e6c4a0f2-134a-46ad-9798-777a023cbc28" />
C1=NC(=C2C(=N1)N(C=N2)[C@H]3[C@@H]([C@@H]([C@H](O3)COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O)O)N 
In that case, please add the link in the project notes 
While not task-specific, since some steps (SRP, SPC, COPII, and Clathrin-mediated transport) will be often used (even if the specific subunits won’t all be used), it is nice to have those GPR rules already put in place and updated when in a GPR spreadsheet that everyone can update/use. Here we can see at a glance what the COPII base coat is, and how the insulin-specific (in this case) coat differs. 
<img width="975" height="604" alt="image" src="https://github.com/user-attachments/assets/0323b2a3-0f3c-489e-bc92-6f0c35ed981a" />
This way we can also easily update the reactions_additions file we add to a task folder (copied from the “current files” folder)
For the reactions we start at task 701, and reactions will have the ID equal to the task number + 00
So MAR70100 is the first reaction added in task 701 (note we start at column G  for adding reactions)
  <img width="975" height="226" alt="image" src="https://github.com/user-attachments/assets/15a106b8-77ff-4b4b-b318-995e9292f528" />
Each reaction has an (unique) ID, a name, a subsystem (try sticking with a few ones consistently, see the example above), a formula (using the specific notation as above, make sure that each substrate/product has a compartment (e.g. insulin[s], or water[r]). The available compartments are as follows: 
<img width="975" height="297" alt="image" src="https://github.com/user-attachments/assets/084a8efd-38c2-49a3-bd51-2607bcae9952" />

The reactions should also have the GPR rule written with gene symbols, and all the way at the end the name of the GPR rule (that we can lookup in the larger GPR rule spreadsheet if necessary).
Similarly for the metabolite_additions file, you grab an empty copy and put it in the task folder, then open it and add the metabolties as we did above. 



 ### Documenting the evidence
   You will then search, puzzle, and document out the case, as well as creating the
      files containing the metabolites and reactions. In case there are any useful (used
      by other groups, such as general pathways) things, add their GPRs directly to the
      GPR sheet in the same spreadsheet.

We are then left with a file that should have: 
The task documentation (insulin_synthesis_task_701), the metabolites_additions file, the reactions_additions file, and the short_notes (short_notes_task_701_insulin_synthesis). 
<img width="975" height="161" alt="image" src="https://github.com/user-attachments/assets/ba0c43ef-5223-4d0b-88cc-146ac1db0a1e" />
IGNORE the old_genes and old_GPR rules files, they are unnecessary for you at this point (the genes I can automatically create from the reactions, and the GPR rules moved to the online spreadsheet)
 The short notes should include all the things we are unsure about, were necessary to note, or might still require further looking into: 
<img width="852" height="667" alt="image" src="https://github.com/user-attachments/assets/0b763a68-a164-4123-9e7b-dcc9c3f82428" />
Then we appear to be done, and we let the second assessor check our work. Meanwhile you can take a quick break, or continue with a new task.
      
### Calling for review
   When you feel like you are done, upload all the files by perfomring the following
     git commands (if you added your files in your git directory): 

   ``` bash
   git add .
   git commit -m "feat(task 701): added first assessment of task 701"
   git pull
   git push
   ```

   Then we change the spreadsheet (and possibly say something in the WhatsApp group,
     or whoever is next to you, in case you are working at the same location). Put your
     status to "Awaiting second assessor", possibly take a break, but don't wait just on
     the second assessor (that might take a while) and move on to the next task. Or in
     case another group is awaiting assessment just like you, you can review their task.
     <img width="975" height="151" alt="image" src="https://github.com/user-attachments/assets/ee9b47ab-b666-4508-9221-43066dec7542" />

     
### Performing review assessment
   Now you are reviewing another group's or person's work; change the status of the
    task to "Second assessor (<your name>)" and; open up git bash and pull
    the changes:

   ``` bash
   git pull
   ```
<img width="975" height="103" alt="image" src="https://github.com/user-attachments/assets/980af18c-0ab0-42f7-83bc-703bd3634be2" />

   You should now see their task folder and documentation appear on your own computer
    and you go through their documentation. 
    Check if you follow all the steps based on the evidence they
    provided, did they miss anything, are there any leaps in logic? Are there things
    that you know (from your own task) that might have not been considered in enough
    detail? 

   Based on the quality of the work (interpretation, completeness), and the
    documentation (logical, no leaps, easily followable), you then write your review in
    a document called "peer_review". Write out clearly what needs to changed or looked
    back into and upload that to the git in the same way as before. That way they can
    address each point, possibly argue with you and summarise the changes they make to
    the documents. Remember to also check their metabolites_ and reactions_ files, as
    eventually my scripts will look into those to grab all the things you defined
    together. Of course if it is all great and no changes are necessary, then you can
    sign-off on this task, and so can they!

   This is a collaborative effort so try to help each other, have a discussion if
    things are unclear, or provide some examples of how you would approach the changes
    you are foreseeing. It is the resposibility of everyone that the quality of the work
    is good; similarly if you see somehting that could be done easier, or might require
    everyone to sit together to decide on a particular standard form, then do so! The
    point of this project, besides getting me valuable cytokine tasks and letting you
    learn a lot about said tasks, is also for you to get experience working in
    moderately sized groups! Work together, do this side by side (and hopefully not all
    from the isolation of your home, although even then you could have a
    teams/slack/discord sever where you guys can discuss with eachother)!
    
   When you are done with the changes, don't forget to add, commit, push the
    peer_review file (and possibly other files you put comments in etc). Then set the
    status to "Awaiting first assessor (second)", and go on with your work!
    <img width="975" height="115" alt="image" src="https://github.com/user-attachments/assets/16c6158e-f328-4202-b345-85d9cae857ba" />


### Making changes
   Hopefully the other person/group notifies you when they finished your review: put
    the status back to "first assessment (<your name>) (second)", copy the documentation
    files you made in the first round and copy them, adding "revision_1" to them, then
    open their peer_review document and go through the comments. Make the changes they
    suggest if you agree, discuss with them if things are unclear, look for more
    evidence if you are sure of your interpretation, and of course you can argue against
    implementing changes if you believe there is good reason to do so (it taking too
    much effort is *not* a good reason, of course). 

<img width="975" height="102" alt="image" src="https://github.com/user-attachments/assets/4535103c-2d6c-4af6-a2f2-5502af8e470f" />

   Implement your changes in the revision files, editing them so that they are a "new"
    final version. Then in a page below their comments in the peer_review file,
    summarise the changes you made, and adress (rebute) why other changes were not
    necessary to implement - this is the same procedure as when attempting to publish
    papers: peer reviewers provide comments, and you make changes and write a rebuttal
    to go together with your new version. 

   Git add, commit, push the files; set the status to "Awaiting second assessor
    (second)" and notify them! Preferably it is the same assessor who goes through your
    work, however if for some reason that cannot happen then with all the available
    documentation it should be possible for someone else to read your original
    documentation, the peer_review document, the changes you made, and evaluate it based
    on those alone!

### Assessing the changes
   Someone or a group made changes, now you go through the usual: git pull, set the
    status to "Second assessment (<your name>)", and go through them.
    <img width="975" height="107" alt="image" src="https://github.com/user-attachments/assets/d5f5d89d-4da5-4ed1-b426-12d06efd3614" />

  Most likely (and
    hopefully) the changes are all sufficient and you can sign off on this task. Of
    course if this is not the case then the procedure continues: you add more to the
    peer_review document with the changes that still need to made. If there is some
    actual disagreement, you can always discuss with other people or maybe we plan a
    meeting to discuss it with me (alternatively send me an email or come by my office).
    Remember, this is not an assessment of you as a person! If it turns out that I
    prefer the arguments of another group, or you might have missed something, that
    isn't any problem - the whole point of this is to learn and improve!

### Signing off the task
   The task is done, both sign off, you make sure the task is properly uploaded,
    everything that could go into the sheet (so commonly used GPRs) is added and you
    potentially debrief with other groups/people in case there were valuable things that
    you learned that might help others as well!
  <img width="975" height="71" alt="image" src="https://github.com/user-attachments/assets/933e99ba-aed8-4569-92ea-6b54111c6678" />
 
  Then it's time to continue the work with
    another task! Some tasks might be easier as they will be very similar to a
    previously finished task. On the other hand those might become boring, and it could
    be more exciting to identify a completely different biosynthesis pathway, that is up
    to you! Also if you performed this as a group, evaluate if it makes sense to keep
    doing it as a group, or if you can divide into smaller groups to cover more ground!


- [Report/presentation](#report-presentation)
  - [Report](#report)
    - [What should it include](#what-should-the-report-include)
    - [Writing tips](#writing-tips)
    - [Feedback](#report-feedback)
  - [Presentation](#presentation)
    - [Organising the presentation](#organising-the-presentation)
    - [Presentation tips](#presentation-tips)
- [Problems](#problems)
