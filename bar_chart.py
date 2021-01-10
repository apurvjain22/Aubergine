import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from A2.sending_mail import SendingMail


class BarChart():
    @classmethod
    def bar_chart(cls, cases):
        fig = plt.figure(figsize=(10, 8))
        plt.bar(cases.keys(), cases.values())
        plt.xticks(rotation=60)
        plt.xlabel("Days")
        plt.ylabel("Number of cases")
        plt.savefig('Bar_chart')
        plt.show(block=False)
        SendingMail.mail()  # sending a mail
