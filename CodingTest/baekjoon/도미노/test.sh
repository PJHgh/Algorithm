RED='\033[0;31m'
GREEN='\033[0;32m'
NO_COLOR='\033[0m'

function log_success { printf "${GREEN}[TEST/SUCCESS] $1${NO_COLOR}\n"; }
function log_failure { printf "${RED}[TEST/FAILURE] $1${NO_COLOR}\n"; }

function assert {
    expected=$1
    actual=$2

    if [ "$expected" == "$actual" ]; then
        log_success "assert $expected == $actual\n"
        return 0
    else
        log_failure "assert $expected == $actual\n"
        return 1
    fi
}

function print {
    x=$1
    printf "$x\n"
}

test1=$(echo "1
3 2
1 2
2 3" | python solution.py)
print $test1
assert $test1 1

test2=$(echo "1
6 7
1 2
2 3
3 1
4 5
5 6
6 4
6 3" | python solution.py)
print $test2
assert $test2 1
