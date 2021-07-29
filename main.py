import os
import csv
from util.post import Post
file_path = r'./data.csv'

# 1. Post Loading
        # read data.csv
        # make post instance by line
        # save instance in post list
# 2. Menu printing
# 3. Write Post
# 4. List Post
# 5. Read Post
# 6. Modify Post
# 7. Del Post
# 8. Save Post

post_list = []

if os.path.exists(file_path):
    print('Loading....')
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
else:
    f = open(file_path, 'w', encoding = 'utf8')
    f.close()

def write_post():
    print("\n\n Write Post")
    title = input("Write Title \n>>>>")
    content = input("Write Content \n>>>>")
    id = post_list[-1].get_id() +1
    post = Post(id,title,content,0)
    post_list.append(post)
    print("Job Complete")

def list_post():
    print('\n\n List')
    id_list = []
    for post in post_list:
        print("Number:", post.get_id())
        print("Title:", post.get_title())
        print("Content:", post.get_content())
        print("views:", post.get_view_count())
        print("")
        id_list.append(post.get_id())
    while True:
        print("Q) Select Post Number (Put -1, Back to menu)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
            elif id == -1:
                break
            else:
                print("There is not Post Number")
        except ValueError:
            print("Please put Integer")

def detail_post(id):
    print("\n\n Detail")
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print("Number:", post.get_id())
            print("Title:", post.get_title())
            print("Content:", post.get_content())
            print("views:", post.get_view_count())
            targetpost = post
    while True:
        print("Q) modify: 1, Delete: 2 (put -1, back to menu)")
        try:
            choice = int(input(">>>"))
            if choice ==1:
                update_post(targetpost)
                break
            elif choice == 2:
                delete_post(targetpost)
                break
            elif choice == -1:
                break
            else:
                print("Error")
        except ValueError:
            print("Please put Integer")
        
def update_post(target_post):
    print("\n\nModify")
    title = input("Put Title\n>>>>")
    content = input("put content\n>>>>")
    target_post.set_post(target_post.id,title,content,target_post.view_count)
    print('Job Complete')


def delete_post(target_post):
    post_list.remove(target_post)
    print("Job Complete")

def save():
    f = open(file_path,'w',encoding='utf8')
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(),post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("Save Complete")



# Menu
while True:
    print('\n\n- Blog -')
    print('- Select Menu -')
    print('1. Write Post')
    print('2. View List')
    print('3. Exit')
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("Please input integer value")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("Exit")
            save()
            break;