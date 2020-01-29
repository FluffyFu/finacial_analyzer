"""
File_name: visualize.py
Author: Fluffy
Date: 01/26/2020
Description: class used to visualize the results.
"""
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


class Visualize:
    """
    Visualize the statement results.
    Args:
        report(financial.Report): credit card reports.
    """
    label_fontsize = 15
    figsize = (12, 8)
    title_size = 20

    def __init__(self, report):
        self._report = report
        self._fig, self._ax = plt.subplots(figsize=self.figsize)

    def vis_summary(self, start, end):
        """
        Visualize spending by category in the given time window.

        Args:
            start(int): start date of the time window (inclusive) in the format
            of yyyymmdd.

            end(int): end date of the time window (inclusive) in the format of
            yyyymmdd.
        """
        summary = self._report.summary(start, end)

        self._ax.barh(summary.Category, summary.Amount)
        self._ax.set_ylabel('Category', fontsize=self.label_fontsize)
        self._ax.set_xlabel('Amount (USD)', fontsize=self.label_fontsize)
        self._ax.set_title('{start} to {end} Spending Summary'.format(start=start, end=end),
                           fontsize=self.title_size)
        plt.show()
