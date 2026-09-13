import hashlib


def welcome_assignment_answers(question):
    if question == (
        "In Slack, what is the secret passphrase posted in the "
        "#lab-python-getting-started channel posted by a TA?"
    ):
        answer = "pcap"

    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    elif question == (
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    ):
        nyu_email = "akg10042@nyu.edu"
        answer = hashlib.sha256(nyu_email.encode("utf-8")).hexdigest()

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Yes"

    elif question == (
        "What layer of the TCP/IP model does the protocol DNS belong to? "
        "- The answer should be an integer number"
    ):
        answer = 7

    elif question == (
        "What layer of the TCP/IP model does the protocol ICMP belong to? "
        "- The answer should be an integer number"
    ):
        answer = 3

    else:
        answer = "ERROR: The question did not match any expected question."

    return answer


if __name__ == "__main__":
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))