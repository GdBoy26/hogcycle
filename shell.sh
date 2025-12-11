is_prime(){
    num=$1

    if (( num <= 1 )); then
        echo "Not Prime"
    fi

    for ((i=2, i*i<=num; i++)); do
        if (( num % i == 0 )); then
            echo "Not Prime"
            return
        fi
    done

    echo "$num is Prime"
}

read -p "Enter a number: " number
is_prime "$number"

check_palendrome(){
    num=$1
    rev=0
    original=$num
    
    while (( num > 0 )); do
        digit=$(( num % 10 ))
        rev=$(( rev * 10 + digit ))
        num=$(( num / 10 ))
    done

    if (( rev == original )); then
        echo "$original is a Palindrome"
    else
        echo "$original is Not a Palindrome"
    fi
}

read -p "Enter a number to check for Palindrome: " pal_number
check_palendrome "$pal_number"

check_armstrong(){
    num=$1
    sum=0
    original=$num
    digits=${#num}

    while (( num > 0 )); do
        digit=$(( num % 10 ))
        power=1

        for (( i=0; i<digits; i++ )); do
            power=$(( power * digit ))
        done

        sum=$(( sum + power ))
        num=$(( num / 10 ))
    done    

    if (( sum == original )); then
        echo "$original is an Armstrong number"
    else
        echo "$original is Not an Armstrong number"
    fi
}

read -p "Enter a number to check for Armstrong: " arm_number
check_armstrong "$arm_number"


decimal_to_base5() {
    echo -n "Base-5 of $1 is: "
    echo "obase=2; $1" | bc
}

read -p "Enter a decimal number: " number
decimal_to_base5 "$number"

decimal_to_base5() {
    echo -n "Base-5 of $1 is: "
    echo "obase=5; $1" | bc
}

read -p "Enter a decimal number: " number
decimal_to_base5 "$number"

base5_to_decimal() {
    echo -n "Decimal of base-5 number $1 is: "
    echo "ibase=5; $1" | bc
}

read -p "Enter a base-5 number: " number
base5_to_decimal "$number"

nano shell.sh
chmod +x shell.sh
./shell.sh