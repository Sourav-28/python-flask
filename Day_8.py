all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']
user={}
user['name']=input("Enter your name: ")
user['email']=input("Enter your email: ")
user['courses']=[]
# print(user)

while True:
    print("Welcome ")
    print("*** Menu ***")
    print("1. Show courses" )
    print("2. My courses")
    print("3. Show profile")
    print("4. Edit profile")
    print("0. Exit")
    ch=int(input("Enter your choice: "))

    if ch==0:
        exit(1)
    elif ch==1:
        for i in range(len(all_courses)):
            print(f'{i+1}. {all_courses[i]}')
        q=int(input("Select one course you want to enroll: "))
        user['courses'].append(all_courses[q-1])
        print("Course enrolled succesfully!")
        all_courses.pop(q-1)
    elif ch==2:
        print("Your enrolled courses are: ")
        for i in range(len(user['courses'])):
            print(f"{i+1}. {user['courses'][i]}")
    elif ch==3:
        for k,v in user.items():
            if k=='courses':
                print(k ,":",end=" ")
                for j in user['courses']:
                    print(j,end=" , ")
                print()
            else:
                print(k,":",v)
    elif ch==4:
        print("Do you want to delete the course: ")
        a=input("press Y or N")
        if a=='Y' or 'y':
            for i in range(len(user['courses'])):
                print(f"{i+1}. {user['courses'][i]}")
            q=int(input("Enter the course you want to delete: "))
            all_courses.append(user['courses'][q-1])
            user['courses'].pop(q-1)
            print("Course deleted succesfully!")
        else:
            continue