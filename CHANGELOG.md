## 0.3.2 - January 6, 2024

Additions:
- Debug mode activation and deactivation depending on what runner script is used

Changes:
- Removed even more unused CSS tags
- Rearranged text on the sections again
- Added horizontal rule between the title and details

## 0.3.1 - January 5, 2024

Additions:
- Added support for a "config_private.json" file that takes precedence over "config.json" for use in development purposes to store server credentials that should not be pushed to the repository. This does not change functionality in most cases.

Changes:
- Priority and status now display next to creation and modification dates in order to fit more to-do items on screen
- Fixed priority sort; items without priority are now last regardless of sorting mode
- Improved readability of the "Priority" text colors
- SCSS/CSS optimizations
- Footer text size no longer relies on header type

## 0.3.0 - January 2, 2024

Additions:
- Error handling relating to the CalDAV server being unavailable
- Priority number names and text color
- Django 5 support
- Horizontal rules added to the top and bottom of the page

Changes:
- Task color now defaults to white (#FFFFFF)
- Text sizes no longer rely on header types

## 0.2.0 - December 4, 2023

Additions:
- Support for task priority with configurable sorting
- Support for task colors
- Support for task status
- Some error handling

Changes:
- Removed navigation bar that was left over from ctclsite-python
- Minor changes to header tags

## 0.1.0 - October 31, 2023

Intial version
