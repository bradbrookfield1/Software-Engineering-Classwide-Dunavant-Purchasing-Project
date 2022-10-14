# Setting up your local repo

```
bash$ git clone git@github.com:Real-UM-EECE-4081/dunavant-purchasing.git
Cloning into 'dunavant-purchasing'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

# Development lifecycle

```
bash$ git checkout -b username-feature-branch-name
# edit files to add features
bash$ git add files-to-be-tracked.txt
bash$ git commit
bash$ git push origin username-feature-branch-name
bash$ git checkout -b username-feature-branch-name-qa
bash$ git rebase origin/qa
bash$ git push origin username-feature-branch-name-qa

# create a Pull Request in GitHub.
# Review, approve, and merge the username-feature-branch-name-qa into qa.

bash$ git co qa
bash$ git pull origin qa

# Test your qa branch locally.
# Changes require cycling through the steps above on the feature branch
# and the “-qa” branch.
# Between incremental releases during testing you can either destroy the “-qa” branch 
# for each “push” or cherry-pick the incremental test changes.
```

# Cherry-pick option

```
# Revert to the feature branch to edit and unit test changes required by the testing
bash$ git co username-feature-branch-name
# edit files and unit test
bash$ git add “files changed”
bash$ git commit
bash$ git log
# copy the commit hash

<<<<<Example>>>>
commit d215d05ce38b74b739651036d0903e8b796cb579
Author: Michael Bartz <michael.bartz@dunavant.com>
Date:   Fri Sep 17 14:23:01 2021 -0500

    fixed validation interface

bash$ git co username-feature-branch-name-qa
bash$ git cherry-pick “commit hash”

# From the example above, “git cherry-pick d215d05ce38b74b739651036d0903e8b796cb579”

bash$ git push origin username-feature-branch-name-qa

# create a new PR in GitHub; review, approve and merge.  Test, etc, etc.

# The cherry-pick option works if there is little or no parallel work happening on the qa branch.
# Using the “destroy” option always works
```

#Destroy option

```
# After merging the “-qa” branch in GitHub, delete the “-qa” branch in both GitHub and your local database.
bash$ git branch -D username-feature-branch-name-qa
bash$ git fetch origin -p
# The fetch operation is a “double check” on the delete and sync’s your local repo and the GitHub repo.

# Rinse and repeat the original steps of testing and creating, pushing, reviewing and merging
# your “throw away” -qa branch.
```
