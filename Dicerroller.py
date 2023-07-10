import random
x="y"

while x=="y":
    random_number=random.randint(1,6)

    if random_number==1:
        print("[--------]")
        print("[        ]")
        print("[   0    ]")
        print("[        ]")
        print("[--------]")

    elif random_number==2:
        print("[--------]")
        print("[0       ]")
        print("[        ]")
        print("[      0 ]")
        print("[--------]")

    elif random_number==3:
        print("[--------]")
        print("[        ]")
        print("[ 0  0 0 ]")
        print("[        ]")
        print("[--------]")

    elif random_number==4:
        print("[--------]")
        print("[ 0   0  ]")
        print("[        ]")
        print("[ 0   0  ]")
        print("[--------]")

    elif random_number==5:
        print("[--------]")
        print("[ 0    0 ]")
        print("[    0   ]")
        print("[ 0    0 ]")
        print("[--------]")

    elif random_number==6:
        print("[--------]")
        print("[ 0 0 0  ]")
        print("[        ]")
        print("[ 0 0 0  ]")
        print("[--------]")

    x=input("Press y to Roll again and press any other key fro Exit")






