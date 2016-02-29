# Biking

def biking_record(record):
    if record == 40:
        print "What a great record!"
    elif record > 40:
        print "You're a real champion!"
    elif 20 < record < 40:
        print "It wasn't so bad!"
    else:
        print "You need to exercise more!"

record = 50
record = biking_record(record)

record = 40
record = biking_record(record)

record = 20
record = biking_record(record)

record = 0
record = biking_record(record)

record = 30
record = biking_record(record)