
# DATE functions

##### NOW function

The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.

See also:

- [NOW function - Microsoft Support](https://support.microsoft.com/en-au/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46)

##### TODAY

The TODAY function is useful when you need to have the current date displayed on a worksheet, regardless of when you open the workbook.

For example, if you know that someone was born in 1963, you might use the following formula to find that person's age as of this year's birthday:

```excel
= YEAR(TODAY())-1963
```

- [Video Tutorial: TODAY and NOW functions in excel](https://youtu.be/9ETguwC7Jnk?si=COwxFgKO5WBe1WKX)

further reading:

- [TODAY function - Microsoft Support](https://support.microsoft.com/en-au/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9)
- [Insert the current date and time in a cell - Microsoft Support](https://support.microsoft.com/en-gb/office/insert-the-current-date-and-time-in-a-cell-b5663451-10b0-40ab-9e71-6b0ce5768138)

#### Task: Extracting Day and Month from a Date in Excel

To extract the day and month from a date in Excel, you can use the following functions:

1. **Day Function**: This function extracts the day of the month from a date.

   ```excel
   =DAY(date)
   ```

   Replace `date` with the cell reference that contains the date (e.g., `A1`).

2. **Month Function**: This function extracts the month from a date.

   ```excel
   =MONTH(date)
   ```

   Similarly, replace `date` with the cell reference.

For example, if cell `A1` contains the date `2025-02-06`, you can use the formulas as follows:

- `=DAY(A1)` will return `6`.
- `=MONTH(A1)` will return `2`. 

**Exercise:** Calculate Age

1. In cell A1, enter a birthdate (e.g., 01/15/1980).
2. In cell B1, use the TODAY function to calculate the age. Subtract the birthdate in A1 from the current date (TODAY) and divide by 365.25 (accounting for leap years). The formula in B1 should look like this:

```excel
=(TODAY() - A1) / 365.25
```

The result in cell B1 will be the age in years.

**Exercise :** Calculate Days Remaining

1. In cell A1, enter a future date (e.g., 12/31/2023).
2. In cell B1, use the TODAY function to calculate the number of days remaining until the date in A1. The formula in B1 should look like this:

```excel
=A1 - TODAY()
```

The result in cell B1 will be the number of days remaining until the future date.

**Exercise:** Write the formula to find the date of the first day of the previous month.

- Type the following forumula in any cell:
  
```excel
=DATE(YEAR(TODAY()), MONTH(TODAY())-1, 1)
```

This formula calculates the date of the first day of the previous month. The DATE() function takes three arguments: the year, the month, and the day.

In this case, we are using the YEAR() and MONTH() functions to get the current year and month, respectively. We then subtract 1 from the month to get the month of the previous month. Finally, we set the day to 1 to get the date of the first day of the previous month.

**Exercise:** Calculate Elapsed Time

You can use the NOW function to calculate the elapsed time between two events.

1. In cell A5, type "Start Time:".
2. In cell B5, enter a start time (e.g., "9:00 AM").
3. In cell A6, type "End Time:".
4. In cell B6, use the following formula to calculate the elapsed time between the start and end times:

```excel
=TEXT(NOW()-B5, "hh:mm")
```

This formula subtracts the start time in cell B5 from the current time provided by NOW and formats the result as "hh:mm".

