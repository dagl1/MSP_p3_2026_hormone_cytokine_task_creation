# Creating cytokine and peptide hormone-releasal metabolic tasks

This document provides the infortation required to succesfully pursue the MSP project and therefore should be read carefully. 
Following this document will hopefully ensure that you can deliver high quality research
that you can look back upon fondly and show others as part of your academic portfolio.

---
### Table of contents

- [Useful resources](#useful-resources)
- [Metabolic Task Analysis](#metabolic-task-analysis)
- [Requirements](#project-requirements)
  - [Git usage](#git-usage) (see [Setting up & using Git](#setting-up-and-using-git) as well)
  - [Documentation](#documentation-procedure)
  - [Quality assessment](#quality-assessment-procedure)
- [Setting up & using Git](#setting-up-and-using-git)
  - [Installing Git](#installing-git)
  - [Cloning repository](#cloning-git-repository)
  - [How to use Git](#using-git)
    - [Git bash](#git-bash)
    - [Github Desktop](#github-desktop)
- [Choosing a task/project management](#project-management)
  - [Example Case](#example-case)
  - [Taking the task](#taking-the-case)
  - [Finding appropriate literature](#finding-appropriate-literature)
  - [Documenting the evidence](#documenting-the-evidence)
  - [Calling for review](#calling-for-review)
  - [Performing review assessment](#performing-review-assessment)
  - [Making changes](#making-changes)
  - [Assessing the changes](#assessing-the-changes)
  - [Signing off the task](#signing-off-the-task)
- [Report/presentation](#final-report-and-presentation)
  - [Report](#report)
    - [What should it include](#what-should-the-report-include)
    - [Writing tips](#writing-tips)
    - [Feedback](#report-feedback)
  - [Presentation](#presentation)
    - [Organising the presentation](#organising-the-presentation)
    - [Presentation tips](#presentation-tips)
- [Problems](#problems)

---

## Useful resources
  - [Google Scholar](https://scholar.google.com) for finding articles (I generally
    prefer googling keywords such as "SEC61 signal peptidase pre-pro-insulin". But after
    finding an article, it is generally interesting to see if any articles that were
    published later, and reference this article, add anything to the topic. New
    discoveries related to a previous one (either disputing previously papers, or adding
    to them) will at least refer to the previous articles. Thus if in 2019 someone found
    that SEC61 is important in pre-pro-insulin, and now we wonder if SEC62 (an
    alternative pathway) is also involved, we might look into the articles that cited
    the article from 2019 by searching for this article in google scholar and clicking:
    "cited by".
  - [Metabolic Atlas](https://metabolicatlas.org) is an online representation of
    Human-GEM, the base metabolic model that we utilise here at MaCSBio. It provides
    some functionality for searching for reactions and genes (remember to search in
    Human-GEM and not in the mouse or fruitfly, as those might not be exactly the same).
    While I don't think there will be too much to see (they don't really deal with
    signalling peptides, hence this project), you might sometimes need to check if a
    specific metabolite exists or a compartment already involves a particular process.
    Currently Metabolic Atlas is presenting Human-GEM 1.19, while we use version 1.17
    with some small in-house modifications; it likely is fine to look up these here.
    Altenatively you can find the Human-GEM 1.17 excel file in the current repository.
  - [Uniprot](https://www.uniprot.org) is a database where one can look up information
    on proteins/genes, including the amino acid (AA) sequence. However the identifiers
    used by uniprot do not match the ones of the model (those eventually need to be in
    Ensembl format). Personally I search Ensembl first, the use uniprot for AA sequences
    and sometimes some additional information. 
  - [Ensembl](https://www.ensembl.org/index.html) This is a huge database where one can
    find genes, their location on the genome, and many many other things. As you will
    see in the [Example Case](#example-case), I use it extensively to find the
    gene-identifiers which is what the model will eventually use, and most
    transcriptomics data (which we use in the [Metabolic Task
    Analysis](metabolic-task-analysis) explained below) uses these identifiers too.
  - [Protein-atlas](https://www.proteinatlas.org) Once you have a candidate gene, you
    can find a lot of additional information on it here. Search for the gene and check
    for instance "tissues" or "cell lines" to find the expression pattern of the
    gene/protein you are looking for. This can be useful if you are wondering if a 
    specific protein is involved in a specific process. For instance in the case of
    insulin biosynthesis, a process which only happens in the pancreatic beta islet
    cells, we might wonder if protein X is involved. Thus if we see that protein X is
    not expressed (on both RNA and protein level) in pancreatic cells - specifically
    islet cells - then we might conclude that it is not involved in that process. Of
    course such data isn't infallible and so if there are articles showing protein X's
    involvement directly, we might have to re-evaluate (or mention this discrepancy in
    the short_notes; see [Documenting the evidence](#documenting-the-evidence)).
  - [STRING](https://string-db.org) is a database which collates evidence on
    interactions between proteins and genes. It provides both the strength and type of
    that evidence, for example gene correlations vs experimental evidence proteins are
    interacting with each other. It is very useful - but generally you cannot solely rely
    on STRING, as even if protein X is together with other proteins involved in your
    process of interest, that doesn't mean that protein X *always* is together. It could
    certainly be the case that protein X forms a complex with Y and Z; but XYZ might not
    be involved in insulin biosynthesis, only YZ are). It is however a good resource to
    get a feeling for the involvement of proteins (for instance if there is no evidence
    at all for a protein to interact with Y and Z, and you cannot find anything about
    protein X directly involved in your process, it is pretty good evidence to not
    include protein X).
  - [Genecards](https://www.genecards.org) Another resource with gene information, I
    personally don't find it particularly useful in most cases, although it does have
    intra-cellular localisation of genes (with evidence scores). Typically the
    information is not specific enough, all subunits or paralogs have similar
    descriptiosn and might use the same reference, which isn't always great. Sometimes
    this is worth looking as there migth be some additional information there - I very
    much recommend looking through it once to see what it could offer or provide
    information on.
  - [Metacyc](https://metacyc.org) has information on known metabolic pathways, which
    might not be as relevant for most tasks you are looking into, but for instance if
    anything like redox signalling or some type of waste products are involved, this
    does become (potentially) interesting. It used to be free, but a year ago it
    suddenly became the case that one had a limited amount of look-ups. Still, it is
    comprehensive website and is good to know about.

  - [Pubchem](https://pubchem.ncbi.nlm.nih.gov) This website contains information on
    compounds and chemicals (but not really peptides). If you need to search for a
    metabolite and add its SMILES (a way of representing its chemical structure in text
    form), this is the place. Other than that, you won't really be using it, but knowing
    it exists is going to be useful in any case.

  - [BRENDA](https://www.brenda-enzymes.org) You might at some point need to look-up
    specific enzymes or their activity, this would be the place. I honestly doubt you
    will ever have to go here - then again, it might be good to know that this exists.

  - Git tutorials: As I would like you to use git, which is scary (it was for me for a
    long time, and I do a lot of computer-related work and programming), especially
    in the beginning. Theoretically if you follow the instructions of commiting,
    pushing, pulling changes, and no-one modifies other peoples' files, then no problems
    should emerge. However you will likely get a "merge conflict" or "commit merge
    changes" popup, which you can google or look into. The links below are there to help
    you (even if it takes a little bit, putting in the effort to have a basic
    understanding of git will likely help you in your future). 

    - [many good links, some included later](https://gist.github.com/jaseemabid/1321592)
    - [a beginner's guide to git commits](https://medium.com/@zacyap/a-beginners-guide-to-git-commits-34185ed2ed8d) 
    - [full git usage guide, this is linking to the saving changes part](https://www.atlassian.com/git/tutorials/saving-changes)
    - [w3schools guide if you prefer their style](https://www.w3schools.com/git/git_commit.asp)
    - [common github errors and solutions](https://medium.com/devops-ai-decoded/common-github-errors-and-solutions-cd464f0db2b5)
    - [often encountered errors](https://graphite.com/guides/debugging-common-git-errors)
    - [git cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
    - [visual guide](https://marklodato.github.io/visual-git-guide/index-en.html)     
    - [simpler git](https://nfarina.com/post/9868516270/git-is-simpler) 
    - [git for the lazy](https://wiki.spheredev.org/index.php/Git_for_the_lazy).


## Metabolic Task Analysis
While understanding metabolic modeling or metabolic task analysis comprehensively is not
important, it might be nice to have a basic conceptual understanding. The type of
metabolic modeling I work on requires all inputs and outputs at the end of the day to
match; this means that if we anywhere have CO2 going into the model, then somewhere CO2
must leave the model as well. Alternatively it can combine with other metabolites, or
split into smaller pieces. So if 2 H20 and 2 CO2 goes in, then after some metabolic
reactions one could get 2 HCO3. This "what goes in, must go out" assumption is called
Steady State, and it allows us to simplify a lot of mathematics. 

Why is that relevant for you to know? Because when you build a task, you need to make
sure that it follows Steady State. A metabolic task is a way we can look at a small part
of metabolism. It works by closing all inputs and outputs to a model (so since nothing
can go in, nothing can go out) and then we very specifically provide inputs and outputs,
and use this to figure out how the model converts the inputs to the outputs. 

An analogy that might be helpful is to think of a metabolic model being a map of a
city, with the buildings representing metabolites, and streets/metro/train, representing
reactions that convert one building into another. In a large city, such a map is large
and difficult to analyse, but metabolic task analysis is basically saying: "go from the
university building, to the Mac Donalds in the city centre." We can then ask: is the
street from A to B relevant to this path?

So a metabolic task that investigates glycolysis would be:
  - In: 1 glucose, 2 ATP, 2 NAD, 4 ADP, 4 phosphate
  - Out: 2 pyruvate, 2 ADP, 2 phoshpate, 2 NAHD, 2 H20, 4 ATP

If we would instead put 2 glucose, but don't change the rest, then more glucose would go
into the model/task, than is going out, which the wouldn't be in Steady State and give
an error.

In your case you will be working on peptides, which are normally not included in
metabolic modeling, and so we will have to simplify things in some ways (which you will
see in the [Example Case](#example-case), for instance the a "fake" reaction which makes
pre-pro-insulin-1 into pre-pro-insulin-2, as we can then link the pre-pro-insulin gene
as the "enzyme" of this reaction; another thing is that at some point we cut away two
amino acids from the peptide chain, and we just let these disappear (this is fine as
long as the model doesn't know those peptide chains existed in the first place).

Metabolic reactions are often catalysed by enzymes, and those are proteins and thus have
genes. We can use the gene expression of all the enzymes involved  to quantify the "path"
that is taken for a particular task. That is why your project focusses on finding out
which specific genes are involved at each step, as we can then compare gene expression
of different samples (think patients), to come to conclusions such as: "patient 1 has
overall more expression of insulin, as well as increased expression of the enzymes
involved in its biosynthesis" or "we see that patient 2 has *much* lower expression of a
specific cleavage enzyme, which would lead to build-up of unfinished pro-insulin; this
is linked to some disease, which we also see in patient 2". 

Your work will enable this analysis by providing the involved enzymes in these
processes! The tasks that we make at the end will be read by my algorithm to automatically 
quantifiy different samples' activity for each task!

## Project requirements

Please adhere to the following manegerial requirements to make the project work
smoothly, speedily, and hopefully without problems:


## Git usage

All group members must create a github account and install git or Github Desktop and 
become collaborators to this repository. **All changes you make during the day
should be committed and pushed to the repository!** This will ensure both a paper-trail 
of your contributions and allows your research to remain easily identifyable; increasing 
the usefulness of the work you will do. See [Setting up & using Git](#setting-up-and-using-git) 
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
(Jelle.bonthuis@maastrichtuniversity.nl, or come by my office (PHS1 B3.007), indicating the
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
- Become collaborator to this Github by sending me the name of your account name, so I
  can send you an invite which you will have to accept on Github (you will see an
  message popup and get an email on the adress you registered).

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



## Project management
Instead of having a separate section explaining the choosing of a task and what to
designate to indicate you are working on a task, I instead decided to merge it all into
the example case below!

### Example Case

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
      
   **Please see the case report I prepared in Task_701_insulin_synthesis, go through it
      carefully**. I wrote it not entirely as I would like to see it from you, some of the
      order and overall flow is not in logical order for someone else to read in the
      future. However this is the order by which I found things, and hope to show how I
      often missed things which when reading/looking up other articles then came to
      light.

  There are some points that aren't inside the document itself (**but please first read the insulin case document and short_notes, as otherwise this might be a little vague**) which are described here:
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

`C1=NC(=C2C(=N1)N(C=N2)[C@H]3[C@@H]([C@@H]([C@H](O3)COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O)O)N`

In that case, please add the link in the project notes 
While not task-specific, since some steps (SRP, SPC, COPII, and Clathrin-mediated transport) will be often used (even if the specific subunits won’t all be used), it is nice to have those GPR rules already put in place and updated when in a GPR spreadsheet that everyone can update/use. Here we can see at a glance what the COPII base coat is, and how the insulin-specific (in this case) coat differs. 
l
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

Of course we also have to add the actual task to the finalised tasks sheet in the spreadsheet, which should be in Steady State (meaning the model must be able to convert all metabolites given the reactions you added, and the inputs and outputs provided as the Task, see [Metabolic Task Analysis](#metabolic-task-analysis)). 

<img width="1522" height="1100" alt="image" src="https://github.com/user-attachments/assets/83afccb8-1d32-4684-9a62-0c709d5b98a5" />

"in lb" and "in ub" refer to the amount of inputs (in your case these will always be the same number, if 2 CO2 goes in, then in lb and ub will both be 2)
"out lb" and "out ub" then refer to the outputs.
We wrote this task in the case document already, but here it is formalised so that my algorithm can read this and automatically analyse the task!

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
    task to "Second assessor (your name)" and; open up git bash and pull
    the changes (remember that if you have any changes on your computer, first add them
    and commit, then pull):

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
    the status back to "first assessment (your name) (second)", copy the documentation
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
   Someone or a group made changes, now you go through the usual: git pull (remember
   that if you made any changes in between, that you git add and commit them, before
   pulling), set the status to "Second assessment (your name)", and go through them.

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


## Final report and presentation
While the work you will do, and the documentation, will be super useful for research
purposes, you will also need to summarise your work and present it to MSP. As they might
not be as interested in the exact details, especially for the presentation the goal
would be to communicate what you have done, and what impact this work will have. For the
report I think having that in there is important too, but here you would also be able to
(in summary) discuss what work you have done, what is still open, and the challenges or
future outlook there is in this work. There are a lot of peptides, and the insulin task
took me a very long time to work out - while it is true that parts are reusable - I would
think you will not have finished all of them at the end. Therefore, I will most likely
let other students coming after you read your report. It would thus be nice if it
includes the things that went well, and which things could go better or which require
extra focus.

### Report
#### What should the report include
These are just suggestions, and we can discuss alternatives in detail (for instance, if
you want a different structure that might be more compatible with your data).

- Introduction: why do we do this, what is the point of metabolic task analysis,
  conceptually how did you go about finding the data, and what is the scope of your
  work.
- Methods: overall approach, project management, standards and resources. Make it clear
  so that together with the information on this Github, any other student can do the same work!
- Results: a summary (potentially with some interesting pathway visuals on which
  hormones/cytokines (generallly) used the same pathways. If you all came together on a
  useful standard way of approaching mulitple tasks, that could be a result too.
- Discussion: How will this be used, what things did you achieve, where were things
  unclear, are there gaps in literature (maybe it turns out that golgi-traffickign
  always appears with weak confidence; thus being a potentially interesting target for
  biologists (who will not read this, but such things are nontheless part of discussions
  in academic reports))? Are there any future outlooks, challenges, and speculative
  ideas to further expand this?

#### Writing-tips
Academic writing, writing well, and writing very well is a difficult skill to learn.
Writing nice prose is something that is difficult, and which should necessarily be your
aim. Instead your aim should be - in order - be specific, be clear, be concise, write
in a nice manner. 

To be specific means to read what you write and **try** to misinterpret it. Things that
happen commonly is the referring to a particular concept, while meaning something
slightly different. It very often is clear what you *mean*, but what you wrote is not
what you meant. Another common problem in being specific, is the switching of topics
halfway through a paragraph, while not explicitly saying so. 

To be clear, remember to keep the amount of not-explained information to a minimum. When
you discuss a new term, quickly resolve any type of uncertainty. Readers have trouble
keeping many things in memory, so if you are going to discuss a new topic X, don't first
discuss all the ways it can be used, how people think about it, and then explain what
X actually is. It is difficult to properly contextualise the arguments you are
providing, if the reader doesn't yet know what X is. Keep the flow of information
limited and try to organise paragraphs together. Additionally remember to string
together topics in a way where one paragraph feels like it leads into the next. And if
it really doesn't, then adress that. Make sure the reader gets the feeling you are aware
of this abrupt change (you could use a sentence like "Viewed from an entirely different
perspective, one might also ..."). 

For writing concise, write your arguments. Then attempt to reduce unnecessary
information or merge sentences together (this is thus on an information level 
where you might be able to get the same point across, without needing both points);
afterwards you go through it and attempt to reduce the amount of words. Certain ways of
saying things are naturally more wordy than others. Think of: "On the other hand" vs
"Alternatively".

For writing well/nice, tips on the actual wording are difficult. What is important is to
make sure that the reader is taken along in the story, that there is some type of
cadence in the rhytm of your sentences and a paragraphs. Don't have too many super short
paragraphs, don't have too many very long paragraphs. Similarly for sentences,
alternate, try to imagine the reader and how they are feeling (potentially saying the
text out loud in their head) while reading your text. Think of natural pauses, and make
sure that you don't repeat yourself in ways that give the feeling you forgot about the
fact you wrote it before. 

This last point is a common occurence: you might have
discussed topic X in a part, then later you reintroduce the topic as if it is the first
time. Such occurences will feel odd and discordant to your readers. It might indicate
that you didn't reread your story, but moreover it indicates that either before it
wasn't necessary to explain, you didn't believe in your explanation from before (which
then means you wasted the readers time), or you might believe the reader forgot (making
assumptions about your reader). If you do want to harkon back to something, you can
always say: "as discussed earlier, topic X plays an important role in ... the current
results further point to such a role".

#### Report feedback
I am somewhat stringent on what I consider good writing - note that I do not mean the
style, there are many things I like do not like, but I acknowledge that much better
writers than me use other styles. Instead I am not particularly forgiving on vague or
incorrect statements (even if I could interpret it in a lenient manner and get what you
are trying to say). My assessment of your report will be done in part to provide you
with feedback that I believe will be useful, and thus I will assess you (at least
related to the feedback you receive, less so the grade) as if you are experts. Good
writing is not dependent on where you are in your academic journey; of course, in
grading I will take into account you are Bachelor students. Nevertheless, I will gladly
provide (a lot) of feedback on your reports if you provide me a draft (which I will
check and provide feedback on within 2 working days). It might then also be nice to have
a meeting to discuss the exact comments.

If you follow this route, and implement changes based on the feedback, then you of
course will be graded well. I will also give an (approximate) grade I would give to any
draft. This sometimes, together with potentially a lot of feedback, can feel very
negative: it is not, these are learning oppertunities, and generally we learn best
through mistakes. 

On rereading, I feel the above makes it sound as if I am going to put a red cross
through your draft, rip it in half, and tell you to do it all over. I assure you that
won't be the case, I have however noticed that in general the feedback you receive by
other tutors is typically tailored to your current level, and as such it might feel
overwhelming to get my feedback. Of course we first have to see, it definitely could be
the case that I say "wow nice work, here are some small pointers"!

### Presentation
With the presentation I think you can go a lot of different ways, although in all cases
the important point will be to focus on communicating the what, the why, and the how.
Other students might not care that much about what exactly you found, although an
overview or visual representation will be nice. What they will care about is
understanding what you did, how that might be useful, what difficulties there were, and
how you overcame them. What will the future hold, how did you document your work, and
provide them with a feeling of understanding on why this was valuable.

#### Organising the presentation
I think here you can do almost whatever, I would just make sure that just like in
writing, the audience is taken by the hand in understanding what is happening. Leave out
unnecessary details, instead make sure that they conceptually feel like they get what
you did. A general structure with intro, methods, results, discussion, might not be as
relevant - we should check what the rubric is, and what requirements there are to the
overal structure.

You should think of questions people might ask: "oh so you just did a literature
review" or "could you not just use available pathways from wikipathways". Make sure to
get before those in your presenation, that way you don't sound defensive, instead making
the audience feel you understand the scope of what you did, and why that is useful. What
it was, and what it wasn't. 
Other questinos you might want to just think an answer to, in case they will be asked
(generally it is easy to think of some common questions, an exercise that is worthwhile
to pursue regardless when making a presentation, as it might point out specific
weaknesses in your story/flow that you can fix already).

#### Presentation-tips
A presentation should feel like a concise story, that is well laid out, and that is
presented with confidence. The audience needs to get the feeling that you fully
understand everything about it. Don't make it sound like more or less than you did, be
honest and believe in the value of your work (if you make it sound bigger than it is,
then that implies you feel the value isn't big enough on its own). 

Don't read from slides, don't read from text, preferably don't even have full text
memorised. Try to instead think of a story in your head, think of what the slide needs
to look like for that story, then during the presenation just tell that story. Of cours
you can (and possibly should) rehearse, but rehearsing and memorising aren't the same.
Don't have too much text on your slides, don't make it too fancy, have clear images, and
most importantly, do not repeat your slides except in special circumstances. This last
part happens a lot in student presentations: a slide names several important processes
involved in something, and the student will (without adding anyting) name them all in
order. Sometimes you can't avoid it, but in most cases you could either add extra text,
or mention something like: "it is involved in several processes, which you can see on
screen, the most important ones are x and y".

I personally think that students spent too much time on making presentations look fancy
instead of just neat. I do admit that many people seem to like colours or creativity in
the presentations they observe, however if that takes seven hours, which could have been
spent on improving the logic or flow of the presentation, I personally doubt its
wortwhileness. Neat looking presentations generally have the same information at the
same location (titles always exactly at the same location at the same font size; text
and images generally having designated locations; if using animations, using the same
general order where they appear (if you go left to right once, keep doing that for all
slides)). This helps with keeping people focussed, as they know where to look and
somewhat what to expect. This then also gives you the ability to conciuosly break this
rhytm to make a point or to point something out. Be conscientious with your story
telling!

#### Problems
I very much hope that there will be no problems during the project, neither between your
collaborative effort, nor with my supervision. For the latter, there is always the
possibility to involve my supervisors (the two people also listed for the project), and
of course discuss things with me. 
For interpersonal problems between you (someone not doing anything, a fight, or anything
else), please contact me (preferably after talking between each other) and I can help to
mediate or see if anything is up. Don't wait till the peer-review stage to come with
accusations or comments. Giving and receiving criticism is difficult and uncomfortable
(generally moreso for the receiving part), however it is an important part of working
together, and in many cases one can do so in a civil manner. Neverthelss my office (PHS1
B3.007)is almost always open, and you can always contact me through email or just walk
by! 



