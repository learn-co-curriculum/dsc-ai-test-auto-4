# 🔎 Lab: 2.4 HAM or PHISH? - NLP for Email Filtering 

## Introduction

Spam emails, which are unsolicited and often bulk messages sent to a large number of recipients, started becoming a problem in the late 1990s. These emails typically contained advertisements, scams, or other forms of unwanted content. Over time, spam became a widespread issue, leading to the development of spam filters and anti-spam measures.

Phishing attacks, on the other hand, began to emerge in the early 2000s. Phishing refers to a type of cyber attack where malicious actors impersonate trustworthy entities or organizations to deceive recipients into disclosing sensitive information, such as passwords, credit card details, or personal data. Phishing emails are designed to appear legitimate and often employ social engineering techniques to trick recipients into taking action that benefits the attackers.

Phishing attacks became increasingly prevalent with the rise of online banking, e-commerce, and other online services that require users to provide sensitive information. Attackers realized that by impersonating trusted entities, they could gain access to valuable data or exploit users for financial gain.

While spam and phishing are distinct concepts, they are often intertwined. Let’s compare the two:

- Phishing attacks may be delivered through spam emails, leveraging the large volume and distribution capabilities of spam campaigns to reach a broader audience.
- However, not all spam emails are phishing attempts, as spam can also include other types of unwanted or irrelevant content.
- Since their emergence, both spam and phishing have continued to evolve and adapt to technological advancements and countermeasures.
- Organizations and individuals employ various strategies, such as email filters, user awareness training, and security measures, to combat both spam and phishing and protect against their threats.
In this exercise, you will use your knowledge of language patterns used by malicious actors and natural language processing techniques that were introduced in previous lessons to classify emails as HAM (legitimate emails) or PHISH (malicious emails). Creating labeled datasets such as these allows us to train models that can classify millions of emails, using the patterns extracted from just a small subset of known malicious emails.

### Lesson Objectives

By the end of this lesson, you will be able to 

- Distinguish between rule-based and machine learning algorithms
- Identify rules to classify suspicious emails
- Determine the steps to build an email classifier

## Email Filtering

Email filtering is a process in which incoming and outgoing emails are analyzed and categorized based on predefined criteria or rules. The purpose of email filtering is to identify and handle emails based on their content, sender, recipient, or other attributes. Filtering can be performed by email servers, email clients, or dedicated email security systems.

In practice, email filtering systems often employ a combination of rule-based and machine learning techniques. Rule-based filters may be used as an initial line of defense to quickly identify and block obvious spam or phishing attempts based on known patterns. Machine learning models can then be employed to further analyze and classify emails based on more complex features and evolving patterns.

In this lesson, we will discuss rule-based and machine learning techniques for email detection. Then, you will practice classifying emails as HAM or PHISH based on your knowledge of phishing email analysis techniques from the previous lesson. Through this exercise, you will learn all the necessary steps for building an email classifier.


## Rule-Based Algorithms

Early email filters utilized user-defined rule-based approaches. Users could set up filters based on specific keywords, email addresses, or other patterns to sort incoming emails into different folders or mark them as spam. These filters relied on manually created rules and lacked sophistication but provided some level of control over unwanted emails.

Rule-based email filtering algorithms rely on predefined sets of rules and conditions to filter emails. These rules are typically created based on known patterns, keywords, or characteristics associated with spam or phishing emails. The filter applies these rules to incoming emails and flags or categorizes them accordingly.

To combat spam, blacklists, and whitelists were introduced. Blacklists contained known spam sources or email addresses, and emails from these sources were blocked or flagged as spam. Conversely, whitelists allowed users to specify trusted email addresses, ensuring that emails from those sources would always be delivered to the inbox.


## Machine Learning Algorithms

In the early 2000s, Bayesian filtering emerged as a more advanced technique. Bayesian filters used statistical algorithms to analyze the textual content of emails and determine the probability of an email being spam based on learned patterns from a training dataset. This approach improved spam detection accuracy by considering the frequency and co-occurrence of words and phrases.

Machine learning approaches for email filtering involve training models on labeled datasets to automatically learn patterns and features indicative of spam or phishing emails. These models can leverage various algorithms, such as decision trees, Naive Bayes, support vector machines (SVM), or more advanced techniques like deep learning with neural networks. The models extract relevant features from email content, metadata, and other contextual information to make predictions about the email's category.

The training process involves providing the model with a dataset of labeled emails, where each email is labeled as spam (emails that are a nuisance), ham (emails that are legitimate), or phish (emails that are malicious). The model learns the patterns and relationships in the data and generalizes them to make predictions on new, unseen emails. Machine learning-based filters have the advantage of adaptability and can learn from evolving spam or phishing tactics. They can improve their accuracy over time as they encounter more examples and update their models.

By combining rule-based algorithms and machine learning techniques, email filters aim to provide a robust and effective solution for detecting and filtering spam and phishing emails, enhancing email security, and reducing the risk to end-users.


## Modern Email Filters

Modern email filters also employ behavioral analysis and heuristics to detect spam, phishing, and other email-based threats. These filters analyze patterns, sender reputation, email headers, and other contextual information to identify suspicious activities, such as large-scale email campaigns or attempts to deceive users. Heuristics-based filters make use of predefined rules and algorithms to evaluate email content and determine its likelihood of being spam or malicious.

Today, effective email filtering systems often combine multiple techniques and approaches. They employ a combination of rule-based filtering, machine learning algorithms, blacklists, whitelists, behavioral analysis, and authentication mechanisms. This integration allows for more accurate and comprehensive detection of spam, phishing attempts, malware, and other email threats.


## What is Pseudo-Code?

In this exercise, you will be tasked with writing a script in pseudo-code that will classify emails as HAM, SPAM, or PHISH. If you are unfamiliar with programming, this might seem like an intimidating task, but the beauty of writing in pseudo-code is that it allows you to articulate the rules that the program should execute in an approachable way.

Pseudo-code is a simplified and human-readable notation that represents the steps and logic of a computer program or algorithm. It uses a combination of plain English language and programming-like constructs to outline the sequence of operations, decision-making processes, loops, and other control structures involved in the program.

Here is a simplified example of a pseudo-code for dispensing a soda from a vending machine:

None

None

**In English, we would interpret this as "When a coin is present in the machine, dispense a soda. Otherwise, do nothing."** 

Pseudocode is not meant to be executed by a computer; instead, it serves as a blueprint for programmers to design and communicate their algorithms. There are no hard and fast rules about the conventions that you use to convey your idea, as long as it is clear to the reader. It is simply a way to help programmers think through the problem-solving process and plan their code implementation before writing the actual code in a specific programming language.


## Email Classification Script

To keep our example simple, we are going to look for three specific types of flags in email text that suggest phishing. Keep in mind that in a professional context, email classification uses a more complex combination of rule-based and machine learning algorithms.

None

None

None

In addition, there are rules about the sequence of events that occur.

- New emails should be quarantined and checked before they are moved to the inbox.
- The text should be preprocessed before using techniques like sentiment analysis or NER.
With these rules in mind,  you will order the pseudo-code lines in the exercise below so that they are in the correct order to classify the emails using the rules described here and your knowledge of NLP, cyber security, and email filtering. 


## Procedure

Work through each of the parts below and order the steps of the email filtering process for each part.

### Part 1 - Preprocess Text

None

Order each of the steps (A-E) in the correct order to accomplish the task.

- `If COUNT(QUARANTINE) > 0 then CHECK_EMAIL = YES`
- `For each EMAIL in QUARANTINE apply CHECK_EMAIL(EMAIL). If CHECK_EMAIL(EMAIL) then EMAIL_TEXT = EXTRACT_TEXT(EMAIL)`
- `While EMAIL = NEW, move EMAIL to QUARANTINE`
- `TOKEN_TEXT = YES`
- `If EMAIL_TEXT = YES then TOKEN_TEXT = TOKENIZE(EMAIL_TEXT)`
<details style="margin-bottom: 2.5rem;">
<summary style="display: inline-block; background: #394a58; border: 1px solid #8A8B99; padding: 0.5rem 0.75rem; cursor: pointer;"><span style="color: #ffffff;">Select for Part 1 </span></summary>
<ol style="list-style-type: decimal;">
<li><code>While EMAIL = NEW, move EMAIL to QUARANTINE</code></li>
<li><code>If COUNT(QUARANTINE) &gt; 0, CHECK_EMAIL = YES</code></li>
<li><code>For each EMAIL in QUARANTINE apply CHECK_EMAIL(EMAIL). If CHECK_EMAIL(EMAIL) then EMAIL_TEXT = EXTRACT_TEXT(EMAIL)</code></li>
<li><code>If EMAIL_TEXT = YES then TOKEN_TEXT = TOKENIZE(EMAIL_TEXT)</code></li>
<li><code>TOKEN_TEXT = YES</code></li>
</ol>
</details>

### Part 2 - NER for Suspicious Entities and Links

None

Order each of the steps (A-E) in the correct order to accomplish the task.

- `If ANY(TOKEN in TOKEN_TEXT) starts with ANY(“Bank of”) or ends with ANY(“Bank”, “Credit Union”) then SUSPICIOUS ENT = YES`
- `If TOKEN_TEXT = YES then NER(TOKEN_TEXT)`
- `If ANY(TOKEN in TOKEN_TEXT) = URL, CHECK_PATTERNS(URL)`
- `If NER(TOKEN_TEXT) then CHECK_PATTERNS(TOKEN_TEXT)`
- `If ANY(TOKEN in URL) starts with ANY(“Bank of”) or ends with ANY(“Bank”, “Credit Union”) then SUSPICIOUS LINK = YES`
<details style="margin-bottom: 2.5rem;">
<summary style="display: inline-block; background: #394a58; border: 1px solid #8A8B99; padding: 0.5rem 0.75rem; cursor: pointer;"><span style="color: #ffffff;">Select for Part 2 </span></summary>
<ol style="list-style-type: decimal;">
<li><code>If TOKEN_TEXT = YES then NER(TOKEN_TEXT)</code></li>
<li><code>If NER(TOKEN_TEXT) then CHECK_PATTERNS(TOKEN_TEXT)</code></li>
<li><code>If ANY(TOKEN in TOKEN_TEXT) starts with ANY(“Bank of”) or ends with ANY(“Bank”, “Credit Union”) then SUSPICIOUS ENT = YES</code></li>
<li><code>If ANY(TOKEN in TOKEN_TEXT) = URL, CHECK_PATTERNS(URL)</code></li>
<li><code>If ANY(TOKEN in URL) starts with ANY(“Bank of”) or ends with ANY(“Bank”, “Credit Union”) then SUSPICIOUS LINK = YES</code></li>
</ol>
</details>

### Part 3 - Sentiment Analysis for Suspicious Messages

None

Order each of the steps (A-C) in the correct order to accomplish the task.

- `If ANY(TOKEN in TOKEN_TEXT) = “URGENT” or “CLICK HERE” then ADJUSTED_SENTIMENT = SENTIMENT - 0.5`
- `If TOKEN_TEXT = YES then ANALYZE_SENTIMENT(TOKEN_TEXT)`
- `If ANALYZE_SENTIMENT(TOKEN_TEXT) then CHECK_TERMS(TOKEN_TEXT)`
<details style="margin-bottom: 2.5rem;">
<summary style="display: inline-block; background: #394a58; border: 1px solid #8A8B99; padding: 0.5rem 0.75rem; cursor: pointer;"><span style="color: #ffffff;">Select for Part 3 </span></summary>
<ol style="list-style-type: decimal;">
<li><code>If TOKEN_TEXT = YES then ANALYZE_SENTIMENT(TOKEN_TEXT)</code></li>
<li><code>If ANALYZE_SENTIMENT(TOKEN_TEXT) then CHECK_TERMS(TOKEN_TEXT)</code></li>
<li><code>If ANY(TOKEN in TOKEN_TEXT) = “URGENT” or “CLICK HERE” then ADJUSTED_SENTIMENT = SENTIMENT - 0.5</code></li>
</ol>
</details>

### Part 4 - HAM OR PHISH? 

Task: Sort the emails based on if they exhibit Flags 1, 2, or 3 (PHISH) or no flags (HAM).

**Order each of the steps (A-D) in the correct order to accomplish the task** 

- `ELSE then HAM`
- `If SUSPICIOUS ENT = YES then PHISH`
- `If SUSPICIOUS LINK = YES then PHISH`
- `If ADJUSTED_SENTIMENT > .05 then PHISH`
<details style="margin-bottom: 2.5rem;">
<summary style="display: inline-block; background: #394a58; border: 1px solid #8A8B99; padding: 0.5rem 0.75rem; cursor: pointer;"><span style="color: #ffffff;">Select for Part 4 </span></summary>
<ol style="list-style-type: decimal;">
<li><code>If SUSPICIOUS ENT = YES then PHISH</code></li>
<li><code>If SUSPICIOUS LINK = YES then PHISH</code></li>
<li><code>If ADJUSTED_SENTIMENT &gt; .05 then PHISH</code></li>
<li><code>ELSE then HAM</code></li>
</ol>
<p><strong><em>Based on our rules, the order of 1, 2, and 3 are interchangeable. </em></strong></p>
</details>


## Summary

In this exercise, you went in-depth in your understanding of email filtering and how language patterns can be used as part of a multi-approach system to detect phishing emails and other suspicious activity. You had an opportunity to identify the correct order of steps for executing a simplified email classifier using natural language processing techniques like sentiment analysis and named entity recognition. 

Throughout this task, you may have noticed that it can take quite a few lines of code to execute a very simple set of rules. This observation is structured to help you appreciate that while rules are an indispensable part of pattern recognition in threat detection, that machine learning techniques are necessary to handle the increasingly complex patterns that suggest suspicious activity. 


