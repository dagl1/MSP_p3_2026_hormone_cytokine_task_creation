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
  - [Asessing the changes](#assessing-the-changes)
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

Below is an example of how a cas

### 

- [Example Case](#example-case)
  - [Taking the task](#taking-the-case)
  - [Finding appropriate literature](#finding-appropriate-literature)
  - [Documenting the evidence](#documenting-the-evidence)
  - [Calling for review](#calling-for-review)
  - [Performing review assessment](#performing-review-assessment)
  - [Making changes](#making-changes)
  - [Asessing the changes](#assessing-the-changes)
  - [Signing off the task](#signing-off-the-task)
