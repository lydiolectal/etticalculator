# Etticalculator

A Calculator Language that enforces politeness. Inspired in part by [INTERCAL](https://en.wikipedia.org/wiki/INTERCAL).

## Etiquette in Etticalculator
The most important part of Etticalculator is etiquette. If you are not exceedingly polite, the calculator will punish you.

### Please
Every line that you want evaluated must be prefaced with "Please." If you do not say "Please", the interpreter will interpret that line as a comment and ignore you. You don't want to be ignored, do you? Good.

```
Please add 2 to 2.
Add 2 to 2. <-- interpreter will ignore this.
```

### Thank you
When you think the calculator has done enough work, you can thank the calculator and receive the most recently evaluated expression. "Thank you" is equivalent to a "print" statement. If you don't thank the calculator, it will do the work but never give you the answer.

You can have multiple "Thank you"s within the program. You can never have too many "Thank you"s. Thank you.

```
Please add 2 to 2. Thank you. <-- prints '4'.
Please add 3 to 4.            <-- won't print.
```

### Profanities
Profanities are vulgar and never tolerated by our calculator.

(However, because our calculator is of such good breeding, it has only been exposed to one profanity and will not recognize others.)

Our calculator will tolerate profanities in comments because it respects your personal space.

However! Our calculator will not tolerate profanities in your commands (i.e., in lines that begin with "Please"). If you do include a profanity in a "Please" line, the interpreter will enter into an infinite loop of sadness and repeatedly print "You hurt me. Calculators have feelings, too."

It will only go into this infinite loop if the profanity is found in an otherwise valid command; if you say `Please fucking dance for me`, our program will simply throw an "invalid syntax error". To swear, you can do any of the following or more:

```
Fucking please add 2 to 3.
Please fucking add 2 to 3.
Fucking please fucking add fucking 2 to fucking 3.
```

## Syntax

There are 4 legal core expressions in this language that can be used to express:
- Addition
- Subtract
- Multiply
- Divide

For example:
```
2 + 3
Please add 2 to 3.

5 - 4
Please subtract 4 from 5.

3 * 3
Please multiply 3 by 3.

15 / 5
Please divide 15 by 5.
```

## Referencing previous operations

In this language, you can only include one operation per line. To perform compound operations (i.e., `(5 + 3) / 2)`, you would reference previous operations by the line number (starting at 1). For instance, to evaluate `(5 + 3) / 2`, we could write:

```
Please add 5 to 3.
Please divide line 1 result by 2. Thank you.
```
This would print `4`.

A slightly more complex example:
```
Please add 2 to 3.
Please subtract 5 from 15.
Please divide line 1 result by line 2 result. Thank you.
Please subtract 6 from line 3 result. Thank you.
```

This would print `0.5` and `-5.5`.

## Minutiae

Empty lines are not permitted. It is rude to waste our calculator's space.

```
Please divide 15 by 3.
                            <-- this is not okay.
Please add 4 to 1.
```

Spaces are fine, just make sure to leave spaces between your words and numbers. (Tabs are ew. Please don't tab.)

We will ignore all capitalization and punctuation, so feel free to ExpREss yoUrself; ~t~ypOGraphi:Ca!Lly~.

To illustrate what we mean, here is a perfectly valid command:

```
p.....l...e....A....S....E!!!!!!!!!!!! ADD 3 to 5!??!?!?!?!?!?!?!!? th!!!ank you?!?!?!?!
```

This is functionally equivalent to:

```
Please add 3 to 5. Thank you.
```
