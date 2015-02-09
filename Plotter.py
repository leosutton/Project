__author__ = 'Leo'
import numpy as np
import matplotlib.pyplot as plt
import collections

class Plotter(object):
    def __init__(self, record):
        self.record = collections.OrderedDict(sorted(record.items(), key=lambda t: t[0]))
        times = []
        nothings = []
        seedEmails = []
        otherEmails = []
        participateds = []
        rejecteds = []

        for key in self.record:
            times.append(key)
            nothings.append(record[key].nothing)
            seedEmails.append(record[key].seedEmail)
            otherEmails.append(record[key].otherEmail)
            participateds.append(record[key].participated)
            rejecteds.append(record[key].rejected)

        print(times)
        print(nothings)
        print(seedEmails)
        print(otherEmails)
        print(participateds)
        print(rejecteds)

        plt.plot(times, nothings, 'r')
        plt.plot(times, seedEmails, 'b')
        plt.plot(times, otherEmails, 'c')
        plt.plot(times, participateds, 'g')
        plt.plot(times, rejecteds)

        plt.show()