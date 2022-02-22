void main(List<String> arguments) {
    print("[+] Dart project was created!\n");

    int a = 0;
    double b = 0.1;
    String c = "string";
    bool d = true;

    print("[+] Variable A: $a");
    print("[+] Variable B: $b");
    print("[+] Variable C: $c");
    print("[+] Variable D: $d\n");

    var number_1 = 15;
    var number_2 = 5;

    print("[+] $number_1 + $number_2: ${number_1 + number_2}");
    print("[+] $number_1 - $number_2: ${number_1 - number_2}\n");
    
    if (number_1 == number_2) {
        print("[+] $number_1 is equal $number_2\n");
    } else {
        print("[-] $number_1 is not equal $number_2\n");
    }

    var result = number_1 == 15 ? 0 : 1;
    print("[+] Result: $result\n");

    var digit = 5;

    switch (digit) {
        case 1:
            print("[+] Digit is equal 1\n");
            break;
        case 5:
            print("[+] Digit is equal 5\n");
            break;
        default:
            print("[+] Default block in switch-case\n");
            break;
    }

    var list = [0, 0.1, "word", true];
    // var list = List();
    // List<int> list = [1, 2, 3];

    list.add(1);
    list.addAll([1, 0.2, "text", false]);

    list.remove(1);
    list.removeAt(0);
    // list.removeWhere((element) => element > 5);

    print("[+] List: $list");
    print("[+] First: ${list.first}, last: ${list.last}, length: ${list.length}\n");

    var set = {1, 2, 3, 4, 5, 6};
    // Set<int> set = {1, 2, 3};
    
    print("[+] Set: $set\n");
    
    for (var i = 0; i < list.length; i++) {
        print("[${i + 1}] Element: ${list[i]}");
    }
    // for (var element in list) {
    //     element++;
    //     print("[${i + 1}] Element: $element");
    // }
    
    // print("\n[+] For-each");
    // list.forEach((element) {
    //     print("[+] $element");
    // });
    
    print("\n[+] While");
    var i = 0;
    while (i < 10) {
        print("[${i + 1}] Number: $i");
        i++;
    }

    print("\n[+] Do-while");
    i = 0;
    do {
        print("[${i + 1}] Number: $i");
        i++;
    } while (i < 10);

    print("\n[+] Function sum: ${sum(2, 3)}");
}

int sum(int a, int b) {
    return a + b;
}

