import os
import json
from pprint import pprint

def export_bookmarks(folder, bookmarks_file, output_file):
    with open(bookmarks_file, encoding="utf-8") as file:
        bookmarks = json.load(file)
        
    bookmark = iterate_through_bookmarks(bookmarks, folder)
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(bookmark, outfile, indent = 4, sort_keys=True)
    
def import_bookmarks(input_file, bookmarks_file):
    with open(input_file, encoding="utf-8") as file:
        imported_bookmarks = json.load(file)

    with open(bookmarks_file, encoding="utf-8") as file:
        bookmarks = json.load(file)

    bookmarks['roots']['bookmark_bar']['children'].append(imported_bookmarks)

    with open(bookmarks_file, "w", encoding="utf-8") as outfile:
        json.dump(bookmarks, outfile, indent = 4, sort_keys=True)

def iterate_through_bookmarks(bookmarks, folder):
    spacer = "      "
    for parent_folder in bookmarks['roots']['bookmark_bar']['children']:
        # print()
        root = 0
            
        line = f"/{parent_folder['name']}"
        # if folder is not None:
        #     print()
        if folder == line:
            bookmark = parent_folder
            print(type(bookmark))
            # print(f"Bookmark: {line}")
            # pprint(bookmark)
            return bookmark

        try:
            for child1 in parent_folder['children']:
                root = 1
                
                # if folder is not None:
                #     line = f"{spacer*root}/{parent_folder['name']}/{child1['name']}"
                #     print(line)
                line = f"{spacer*root}/{parent_folder['name']}/{child1['name']}"
                line_raw = f"/{parent_folder['name']}/{child1['name']}"
                if folder == line_raw:
                    bookmark = child1
                    # print(f"Bookmark: {line}")
                    # pprint(bookmark)
                    return bookmark

                for child2 in child1['children']:
                    root = 2
                    # if folder is not None:
                    #     line = f"{spacer*root}/{parent_folder['name']}/{child1['name']}/{child2['name']}"
                    #     print(line)
                    line = f"{spacer*root}/{parent_folder['name']}/{child1['name']}/{child2['name']}"
                    line_raw = f"/{parent_folder['name']}/{child1['name']}/{child2['name']}"
                    if folder == line_raw:
                        bookmark = child2
                        # print(f"Bookmark: {line}")
                        # pprint(bookmark)
                        return bookmark
                    
                    try:
                        for child3 in child2['children']:
                            root = 3

                            # if folder is not None:
                                
                            #     print(line)
                            line = f"{spacer*root}/{parent_folder['name']}/{child1['name']}/{child2['name']}/{child3['name']}"
                            line_raw = f"/{parent_folder['name']}/{child1['name']}/{child2['name']}/{child3['name']}"
                            if folder == line_raw:
                                bookmark = child3
                                # print(f"Bookmark: {line}")
                                # pprint(bookmark)
                                return bookmark

                    except KeyError as e:
                            pass
        except KeyError as e:
                pass

def main():
    USERNAME = os.environ.get('USERNAME')
    bookmarks_file = f"C:/Users/{USERNAME}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Bookmarks"
    bookmarks_file_write = f"C:/Users/{USERNAME}/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks"

    mode = input("Select mode (import/export): ")
    if mode == "export":
        folder = input("Which folder do you want to export? (Ex: /Banking/Credit Cards): ")
        output_file = "bookmarks.txt"
        export_bookmarks(folder, bookmarks_file, output_file)
    elif mode == "import":
        input_file = "bookmarks.txt"
        import_bookmarks(input_file, bookmarks_file_write)
    else:
        print("Invalid mode. Please enter 'import' or 'export'.")

if __name__ == "__main__":
    main()
