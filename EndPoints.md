# PyKavita
## A Python Wrapper API for Kavita

A list of Endpoints that are available for Kavita (as of 0.5) that I intend to support.
NOTE: This does not include the OPDS endpoints.

If the Endpoint is listed in **BOLD** then it has full support. If it's listed in _italics_ then it has partial support. ***BOLD ITALICS*** means it has full support with a condition.
Methods that are bolded are supported.
If you want to learn any more about the endpoints listed below, a swagger.json is in this repo that this file is based off.

### Current Endpoints
#### Account
Unlikely to support any of these other than /roles as they're meant for interaction from the user rather than a script. Let me know if you want these and I can look into adding them.
* /api/Account/reset-password - post
* /api/Account/register - post
* /api/Account/login - post
* /api/Account/refresh-token - post
* /api/Account/roles - get
* /api/Account/update-rbs - post
* /api/Account/reset-api-key - post

#### Admin
Won't support this. For this to ever not be True, you'd have to be going through first time setup. You wouldn't even be able to reach this as you wouldn't yet have an API key.
* /api/Admin/exists - get

#### Book
* /api/Book/{chapterId}/book-info - get     
* /api/Book/{chapterId}/book-resources - get
* /api/Book/{chapterId}/chapters - get      
* /api/Book/{chapterId}/book-page - get

#### Collection
* /api/Collection - get
* /api/Collection/search - get
* /api/Collection/update - post
* /api/Collection/update-for-series - post
* /api/Collection/update-series - post

#### Download
* /api/Download/volume-size - get
* /api/Download/chapter-size - get
* /api/Download/series-size - get
* /api/Download/volume - get
* /api/Download/chapter - get
* /api/Download/series - get
* /api/Download/bookmarks - post

#### Image
* /api/Image/chapter-cover - get
* /api/Image/volume-cover - get
* /api/Image/series-cover - get
* /api/Image/collection-cover - get
* /api/Image/bookmark - get

#### Library
* /api/Library/create - post
* /api/Library/list - get
* /api/Library - get
* /api/Library/grant-access - post
* **/api/Library/scan** - **post**
* /api/Library/refresh-metadata - post
* /api/Library/libraries - get
* /api/Library/delete - delete
* /api/Library/update - post
* /api/Library/search - get
* /api/Library/type - get

#### Metadata
* /api/Metadata/genres - get
* /api/Metadata/people - get
* /api/Metadata/tags - get
* /api/Metadata/age-ratings - get
* /api/Metadata/publication-status - get
* /api/Metadata/languages - get

#### Plugin
* **/api/Plugin/authenticate** - **post** - Returns the authorisation that this module initially used to authenticate, so may be dated if information has changed since initial authentication.

#### Reader
* /api/Reader/image - get
* /api/Reader/chapter-info - get
* /api/Reader/mark-read - post
* /api/Reader/mark-unread - post
* /api/Reader/mark-volume-unread - post
* /api/Reader/mark-volume-read - post
* /api/Reader/mark-multiple-read - post
* /api/Reader/mark-multiple-unread - post
* /api/Reader/mark-multiple-series-read - post
* /api/Reader/mark-multiple-series-unread - post
* /api/Reader/get-progress - get
* /api/Reader/progress - post
* /api/Reader/continue-point - get
* /api/Reader/has-progress - get
* /api/Reader/mark-chapter-until-as-read - post
* /api/Reader/get-bookmarks - get
* /api/Reader/get-all-bookmarks - get
* /api/Reader/remove-bookmarks - post
* /api/Reader/get-volume-bookmarks - get
* /api/Reader/get-series-bookmarks - get
* /api/Reader/bookmark - post
* /api/Reader/unbookmark - post
* /api/Reader/next-chapter - get
* /api/Reader/prev-chapter - get

#### ReadingList
* /api/ReadingList - get, delete
* /api/ReadingList/lists - post
* /api/ReadingList/items - get
* /api/ReadingList/update-position - post
* /api/ReadingList/delete-item - post
* /api/ReadingList/remove-read - post
* /api/ReadingList/create - post
* /api/ReadingList/update - post
* /api/ReadingList/update-by-series - post
* /api/ReadingList/update-by-multiple - post
* /api/ReadingList/update-by-multiple-series - post
* /api/ReadingList/update-by-volume - post
* /api/ReadingList/update-by-chapter - post
* /api/ReadingList/next-chapter - get
* /api/ReadingList/prev-chapter - get

#### Series
* /api/Series - post
* _/api/Series/{seriesId}_ - **get**, delete
* /api/Series/delete-multiple - post
* /api/Series/volumes - get
* /api/Series/volume - get
* /api/Series/chapter - get
* /api/Series/update-rating - post
* /api/Series/update - post
* /api/Series/recently-added - post
* /api/Series/all - post
* /api/Series/on-deck - post
* /api/Series/refresh-metadata - post
* **/api/Series/scan** - **post**
* _/api/Series/metadata_ - **get**, post
* /api/Series/series-by-collection - get
* /api/Series/series-by-ids - post
* /api/Series/age-rating - get

#### Server
* /api/Server/restart - post - Reported as not currently working, no intention to support.
* **/api/Server/clear-cache** - **post**
* **/api/Server/backup-db** - **post**
* **/api/Server/server-info** - **get**
* /api/Server/logs - get - Currently returns some garbled data, may not support.
* /api/Server/check-update - get
* /api/Server/changelog - get

#### Settings
* /api/Settings/base-url - get
* /api/Settings - get, post
* /api/Settings/reset - post
* /api/Settings/task-frequencies - get
* /api/Settings/library-types - get
* /api/Settings/log-levels - get
* /api/Settings/opds-enabled - get
* /api/Settings/authentication-enabled - get

#### Upload
* /api/Upload/series - post
* /api/Upload/collection - post
* /api/Upload/chapter - post
* /api/Upload/reset-chapter-lock - post

#### Users
* /api/Users/delete-user - delete
* /api/Users - get
* /api/Users/names - get
* /api/Users/has-reading-progress - get
* /api/Users/has-library-access - get
* /api/Users/update-preferences - post