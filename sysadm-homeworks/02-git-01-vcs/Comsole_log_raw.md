(python312) PS C:\devops-36> git config --list --show-origin
file:C:/Program Files/Git/etc/gitconfig diff.astextplain.textconv=astextplain
file:C:/Program Files/Git/etc/gitconfig filter.lfs.clean=git-lfs clean -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.smudge=git-lfs smudge -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.process=git-lfs filter-process
file:C:/Program Files/Git/etc/gitconfig filter.lfs.required=true
file:C:/Program Files/Git/etc/gitconfig http.sslbackend=openssl
file:C:/Program Files/Git/etc/gitconfig http.sslcainfo=C:/Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt
file:C:/Program Files/Git/etc/gitconfig core.autocrlf=true
file:C:/Program Files/Git/etc/gitconfig core.fscache=true
file:C:/Program Files/Git/etc/gitconfig core.symlinks=false
file:C:/Program Files/Git/etc/gitconfig core.editor=nano.exe
file:C:/Program Files/Git/etc/gitconfig pull.rebase=false
file:C:/Program Files/Git/etc/gitconfig diff.astextplain.textconv=astextplain
file:C:/Program Files/Git/etc/gitconfig filter.lfs.clean=git-lfs clean -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.smudge=git-lfs smudge -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.process=git-lfs filter-process
file:C:/Program Files/Git/etc/gitconfig filter.lfs.required=true
file:C:/Program Files/Git/etc/gitconfig diff.astextplain.textconv=astextplain
file:C:/Program Files/Git/etc/gitconfig filter.lfs.clean=git-lfs clean -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.smudge=git-lfs smudge -- %f
file:C:/Program Files/Git/etc/gitconfig filter.lfs.process=git-lfs filter-process
file:C:/Program Files/Git/etc/gitconfig filter.lfs.required=true
file:C:/Program Files/Git/etc/gitconfig http.sslbackend=openssl
file:C:/Program Files/Git/etc/gitconfig http.sslcainfo=C:/Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt
file:C:/Program Files/Git/etc/gitconfig core.autocrlf=true
file:C:/Program Files/Git/etc/gitconfig core.fscache=true
file:C:/Program Files/Git/etc/gitconfig core.symlinks=false
file:C:/Program Files/Git/etc/gitconfig core.editor=nano.exe
file:C:/Program Files/Git/etc/gitconfig pull.rebase=false
file:C:/Program Files/Git/etc/gitconfig credential.helper=manager
file:C:/Program Files/Git/etc/gitconfig credential.https://dev.azure.com.usehttppath=true
file:C:/Program Files/Git/etc/gitconfig init.defaultbranch=master
file:C:/Users/u3buh/.gitconfig  user.email=mk_0@bk.ru
file:C:/Users/u3buh/.gitconfig  user.name=mikhailk
file:C:/Users/u3buh/.gitconfig  safe.directory=%(prefix)///wsl.localhost/Ubuntu/home/mikhailk/devops-netology
file:C:/Users/u3buh/.gitconfig  safe.directory=C:/devops-36
file:.git/config        core.repositoryformatversion=0
file:.git/config        core.filemode=false
file:.git/config        core.bare=false
file:.git/config        core.logallrefupdates=true
file:.git/config        core.symlinks=false
file:.git/config        core.ignorecase=true
file:.git/config        remote.origin.url=git@github.com:Mikhail-K-devops/devops-36.git
file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
file:.git/config        ssh.variant=ssh
file:.git/config        branch.main.remote=origin
file:.git/config        branch.main.merge=refs/heads/main
(python312) PS C:\devops-36> git add --help
(python312) PS C:\devops-36> git add --help > nano
(python312) PS C:\devops-36> git --help           
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
(python312) PS C:\devops-36> git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
(python312) PS C:\devops-36> git --help git
(python312) PS C:\devops-36> git add *
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
(python312) PS C:\devops-36> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .idea/devops-36.iml
        modified:   .idea/misc.xml
        new file:   01.devpy-main/4.collections/DEV.py
        modified:   01.devpy-main/4.collections/main.py
        modified:   01.devpy-main/4.collections/task3_queries.py
        modified:   GIT commands my2.txt
        new file:   nano
        modified:   sysadm-homeworks/02-git-01-vcs/README.md
        new file:   sysadm-homeworks/02-git-01-vcs/git-add.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/git.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/img/1.jpg

(python312) PS C:\devops-36> rm nano
(python312) PS C:\devops-36> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .idea/devops-36.iml
        modified:   .idea/misc.xml
        new file:   01.devpy-main/4.collections/DEV.py
        modified:   01.devpy-main/4.collections/main.py
        modified:   01.devpy-main/4.collections/task3_queries.py
        modified:   GIT commands my2.txt
        new file:   nano
        modified:   sysadm-homeworks/02-git-01-vcs/README.md
        new file:   sysadm-homeworks/02-git-01-vcs/git-add.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/git.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/img/1.jpg

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    nano

(python312) PS C:\devops-36> git add * 
(python312) PS C:\devops-36> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .idea/devops-36.iml
        modified:   .idea/misc.xml
        new file:   01.devpy-main/4.collections/DEV.py
        modified:   01.devpy-main/4.collections/main.py
        modified:   01.devpy-main/4.collections/task3_queries.py
        modified:   GIT commands my2.txt
        modified:   sysadm-homeworks/02-git-01-vcs/README.md
        new file:   sysadm-homeworks/02-git-01-vcs/git-add.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/git.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/img/1.jpg

(python312) PS C:\devops-36> git diff sysadm-homeworks/02-git-01-vcs/README.md
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index 89d0510..25c022f 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -98,7 +98,8 @@

 ***
 > ### Mikhail K
-> - **(./git.pdf)**
+> - [git help](./git.pdf)
+> - [git add help](./git-add.pdf)
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index 89d0510..25c022f 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -98,7 +98,8 @@

 ***
 > ### Mikhail K
-> - **(./git.pdf)**
+> - [git help](./git.pdf)
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index 89d0510..25c022f 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -98,7 +98,8 @@

 ***
 > ### Mikhail K
-> - **(./git.pdf)**
+> - [git help](./git.pdf)
+> - [git add help](./git-add.pdf)
:...skipping...
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index 89d0510..25c022f 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -98,7 +98,8 @@

 ***
 > ### Mikhail K
-> - **(./git.pdf)**
+> - [git help](./git.pdf)
+> - [git add help](./git-add.pdf)
 ***

 ----
(python312) PS C:\devops-36> git diff sysadm-homeworks/02-git-01-vcs/README.md --staged
fatal: option '--staged' must come before non-option arguments
(python312) PS C:\devops-36> git diff --staged sysadm-homeworks/02-git-01-vcs/README.md 
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index e4d11f4..89d0510 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -3,7 +3,10 @@
 ### Цель задания

 В результате выполнения этого задания вы научитесь подготоваливать новый репозиторий к работе, а также сохранять, перемещать и удалять файлы в системе контроля версий.
-
+***
+> ### Mikhail K
+> - https://github.com/Mikhail-K-devops/devops-36.git
+***


@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~
~

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~
~
~

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~
~
~
~

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~
~
~
~
~
(END)

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
 Чтобы начать знакомиться с документацией просто выполните в консоли команды `git --help`, `git add --help` и изучите их вывод.

+***
+> ### Mikhail K
+> - **(./git.pdf)**
+***
+
 ----

 ### Правила приема домашнего задания
~
~
~
~
~
~
(END)
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index e4d11f4..89d0510 100644
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index e4d11f4..89d0510 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -3,7 +3,10 @@
 ### Цель задания

 В результате выполнения этого задания вы научитесь подготоваливать новый репозиторий к работе, а также сохранять, перемещать и удалять файлы в системе контроля версий.
-
+***
+> ### Mikhail K
+> - https://github.com/Mikhail-K-devops/devops-36.git
+***

 ### Чеклист готовности к домашнему заданию

@@ -93,6 +96,11 @@
 Один из основных навыков хорошего специалиста это уметь самостоятельно находить ответы на возникшие вопросы.
:
diff --git a/sysadm-homeworks/02-git-01-vcs/README.md b/sysadm-homeworks/02-git-01-vcs/README.md
index e4d11f4..89d0510 100644
--- a/sysadm-homeworks/02-git-01-vcs/README.md
+++ b/sysadm-homeworks/02-git-01-vcs/README.md
@@ -3,7 +3,10 @@
 ### Цель задания

 В результате выполнения этого задания вы научитесь подготоваливать новый репозиторий к работе, а также сохранять, перемещать и удалять файлы в системе контроля версий.
-
+***
+> ### Mikhail K
+> - https://github.com/Mikhail-K-devops/devops-36.git
+***

 ### Чеклист готовности к домашнему заданию

@@ -93,6 +96,11 @@
(python312) PS C:\devops-36> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .idea/devops-36.iml
        modified:   .idea/misc.xml
        new file:   01.devpy-main/4.collections/DEV.py
        modified:   01.devpy-main/4.collections/main.py
        modified:   01.devpy-main/4.collections/task3_queries.py
        modified:   GIT commands my2.txt
        modified:   sysadm-homeworks/02-git-01-vcs/README.md
        new file:   sysadm-homeworks/02-git-01-vcs/git-add.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/git.pdf
        new file:   sysadm-homeworks/02-git-01-vcs/img/1.jpg

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sysadm-homeworks/02-git-01-vcs/README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sysadm-homeworks/02-git-01-vcs/img/2.jpg
        sysadm-homeworks/02-git-01-vcs/img/3.jpg

(python312) PS C:\devops-36> git add *
warning: in the working copy of 'sysadm-homeworks/02-git-01-vcs/README.md', LF will be replaced by CRLF the next time Git touches it
(python312) PS C:\devops-36> git commit -m 'First commit'
[main ea62af4] First commit
 13 files changed, 125 insertions(+), 4 deletions(-)
 create mode 100644 01.devpy-main/4.collections/DEV.py
 create mode 100644 sysadm-homeworks/02-git-01-vcs/git-add.pdf
 create mode 100644 sysadm-homeworks/02-git-01-vcs/git.pdf
 create mode 100644 sysadm-homeworks/02-git-01-vcs/img/1.jpg
 create mode 100644 sysadm-homeworks/02-git-01-vcs/img/2.jpg
 create mode 100644 sysadm-homeworks/02-git-01-vcs/img/3.jpg
 create mode 100644 sysadm-homeworks/02-git-01-vcs/img/4.jpg
(python312) PS C:\devops-36> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(python312) PS C:\devops-36> git diff
(python312) PS C:\devops-36> git diff --staged
(python312) PS C:\devops-36> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
(python312) PS C:\devops-36> git add .gitignore  
(python312) PS C:\devops-36> git status        
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore

(python312) PS C:\devops-36> git add *         
(python312) PS C:\devops-36> git commit -m 'Added gitignore'
[main 96fba0b] Added gitignore
 1 file changed, 2 insertions(+)
(python312) PS C:\devops-36> git add *                      
(python312) PS C:\devops-36> git commit -m 'Prepare to delete and move'
[main 2db3347] Prepare to delete and move
 2 files changed, 2 insertions(+)
 create mode 100644 sysadm-homeworks/02-git-01-vcs/img/will_be_moved.txt
 create mode 100644 sysadm-homeworks/02-git-01-vcs/will_be_deleted.txt
(python312) PS C:\devops-36> rm /sysadm-homeworks/02-git-01-vcs/img/will_be_moved.txt
rm : Не удается найти путь "C:\sysadm-homeworks\02-git-01-vcs\img\will_be_moved.txt", так как он не существует.
строка:1 знак:1
+ rm /sysadm-homeworks/02-git-01-vcs/img/will_be_moved.txt
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\sysadm-homew...ll_be_moved.txt:String) [Remove-Item], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.RemoveItemCommand

(python312) PS C:\devops-36> rm ./sysadm-homeworks/02-git-01-vcs/will_be_deleted.txt 
(python312) PS C:\devops-36> mv ./sysadm-homeworks/02-git-01-vcs/img/will_be_moved.txt  ./sysadm-homeworks/02-git-01-vcs/has_been_moved.txt   
(python312) PS C:\devops-36> git add *                                                                                                     
(python312) PS C:\devops-36> git commit -m 'Moved and deleted'                                                                             
[main 0566dbd] Moved and deleted
 2 files changed, 1 deletion(-)
 rename sysadm-homeworks/02-git-01-vcs/{img/will_be_moved.txt => has_been_moved.txt} (100%)
 delete mode 100644 sysadm-homeworks/02-git-01-vcs/will_be_deleted.txt
(python312) PS C:\devops-36> git log
commit 0566dbd9470f200a097cde99993c26defc2be9f9 (HEAD -> main)
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 23 23:48:55 2023 +0300

    Moved and deleted

commit 2db334792bb52a1995eaf6555ce0428697d3dcb7
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 23 23:45:45 2023 +0300

    Prepare to delete and move

commit 96fba0bd8a932ef01e29562cb862f77a1bc4d262
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 23 23:44:26 2023 +0300

    Added gitignore

commit ea62af4232dfe6e4f5407e7248b64f205311bee9
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 23 23:23:37 2023 +0300

    First commit

commit 444614e381080ad624a5f71ef6644d38d2084324 (origin/main)
Author: mikhailk <mk_0@bk.ru>
Date:   Mon Nov 13 23:03:36 2023 +0300

    01.devpy-main.2, 01.devpy-main.3, 01.devpy-main.3 Fixes

commit 09703cc0deaf1416b21e4bb1cc922a5bad4450ab
Author: mikhailk <mk_0@bk.ru>
Date:   Sun Nov 12 23:43:09 2023 +0300

    add 01.devpy-main/4.colelctions homework

commit d547dcd6c2b79580786f1b7e1736a6f43c871398
Author: mikhailk <mk_0@bk.ru>
Date:   Sun Nov 12 23:40:36 2023 +0300

    add 01.devpy-main/4.colelctions homework

commit 5de22a577b07a1305bf975b1f52e05a9e0591c27
Merge: fdf21e5 7edd1aa
Author: mikhailk <mk_0@bk.ru>
Date:   Fri Nov 3 02:32:07 2023 +0300

    Merge branch 'main' of github.com:Mikhail-K-devops/devops-36

commit fdf21e5f9173be80c1df43842d621bb6a5b6c679
Author: mikhailk <mk_0@bk.ru>
Date:   Fri Nov 3 02:19:49 2023 +0300

    3ed Commit

commit 7edd1aad88f4a2fbc4046c65e29dbfc518d73edb
Author: Mikhail Kovalenko <69962484+Mikhail-K-devops@users.noreply.github.com>
Date:   Thu Nov 2 23:24:15 2023 +0300

    Create test

commit 9c75ad41c64a225276fbe417742937ab2589702d
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 2 23:13:48 2023 +0300

    2nd commit

commit 9c11b5924143ff1d8035c570c025896c421f5fa2
Author: mikhailk <mk_0@bk.ru>
Date:   Thu Nov 2 04:42:23 2023 +0300

    first commit
(python312) PS C:\devops-36> git pish
git: 'pish' is not a git command. See 'git --help'.

The most similar command is
        push
(python312) PS C:\devops-36> git push
Enumerating objects: 49, done.
Counting objects: 100% (49/49), done.
Delta compression using up to 16 threads
Compressing objects: 100% (33/33), done.
Writing objects: 100% (35/35), 1.03 MiB | 4.47 MiB/s, done.
Total 35 (delta 18), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (18/18), completed with 10 local objects.
To github.com:Mikhail-K-devops/devops-36.git
   444614e..0566dbd  main -> main
(python312) PS C:\devops-36>
