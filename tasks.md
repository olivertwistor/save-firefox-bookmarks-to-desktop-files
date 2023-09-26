# Tasks

In this document, we keep track of both a work breakdown structure and a network diagram.

## Work breakdown structure

| ID   | Name                                                         | Priority | Depends upon |
| ---- | ------------------------------------------------------------ | -------- | ------------ |
| 1    | Write new repo docs                                          | 1        |              |
| 2    | Read a JSON file containing Firefox bookmarks into memory    | 1        |              |
| 3    | For each bookmark folder, create a new folder on the file system | 1        | 2            |
| 4    | For each bookmark, create a new desktop file with a URL      | 1        | 3            |
| 5    | Remove any bookmarks that have been successfully saved to a desktop file | 2        | 4            |

## Network diagram

| ID   | Name | Priority | Depends upon |
| ---- | ---- | -------- | ------------ |
| 1    | Write new repo docs                                          | 1        |              |
| 2    | Read a JSON file containing Firefox bookmarks into memory    | 1        |              |
| 3    | For each bookmark folder, create a new folder on the file system | 1        | 2            |
| 4    | For each bookmark, create a new desktop file with a URL      | 1        | 3            |
| 5    | Remove any bookmarks that have been successfully saved to a desktop file | 2        | 4            |
