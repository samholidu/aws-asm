import samasm as a
import sys

def main():
    aws_secret_key = sys.argv[1]
    aws_secret_value = sys.argv[2]
    secret_key = a.FetchSecret(aws_secret_key)
    secret_value = a.FetchSecret(aws_secret_value)
    print("\nSecret Key: " + secret_key)
    print("Secret Value: " + secret_value)


if __name__ == '__main__':
    main()