# **Assignment 1: Web Application Mimicking Google Sheets**

## Project Overview:
This project aims to develop a web application that closely mimics the user interface and core functionalities of Google Sheets. The application includes features for spreadsheet-like data manipulation, mathematical functions, data quality checks, and an interactive user interface that supports data entry and visualizations.

## Features:
1. **Spreadsheet Interface:**
   - Mimics Google Sheets UI with a formula bar, toolbar, and cell structure.
   - Allows dragging cell content, formulas, and selections.
   - Supports basic cell formatting (bold, italics, font size, and color).
   - Users can add, delete, and resize rows and columns.

2. **Mathematical Functions:**
   - Implements the following mathematical functions:
     - **SUM:** Calculates the sum of a range of cells.
     - **AVERAGE:** Calculates the average of a range of cells.
     - **MAX:** Returns the maximum value from a range of cells.
     - **MIN:** Returns the minimum value from a range of cells.
     - **COUNT:** Counts the number of cells with numerical values in a range.

3. **Data Quality Functions:**
   - Implements data quality functions like:
     - **TRIM:** Removes leading and trailing whitespace from a cell.
     - **UPPER:** Converts the text in a cell to uppercase.
     - **LOWER:** Converts the text in a cell to lowercase.
     - **REMOVE_DUPLICATES:** Removes duplicate rows from a selected range.
     - **FIND_AND_REPLACE:** Allows users to find and replace specific text within a range.

4. **Data Entry and Validation:**
   - Supports various data types, including numbers, text, and dates.
   - Provides basic validation checks, such as ensuring numeric cells contain only numbers.

5. **Testing:**
   - Provides users the ability to test implemented functions with their own data and clearly displays the results of function execution.

## Bonus Features:
- Support for more complex formulas and cell referencing (e.g., relative and absolute references).
- Allow users to save and load their spreadsheets.
- Incorporation of data visualization capabilities (e.g., charts and graphs).

## Evaluation Criteria:
- **Fidelity to Google Sheets UI:** How well the interface mimics Google Sheets.
- **Functionality:** Completeness of features, including formulas and cell dependencies.
- **Accuracy:** Correct implementation of mathematical and data quality functions.
- **Usability:** Intuitiveness of the UI and ease of use.
- **Code Quality:** Clean and maintainable code.
- **Bonus Features:** Implementation of additional functionalities like saving/loading spreadsheets and advanced data visualizations.

## Technologies Used:
- HTML, CSS, JavaScript for the frontend.
- DOM manipulation for handling dynamic user interactions.
- Mathematical functions implemented using JavaScript.

---

# **Assignment 2: Building a Support Agent Chatbot for CDP**

## Project Overview:
This project involves developing a chatbot that provides support for answering "how-to" questions related to Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot fetches and processes relevant information from the official documentation of these platforms to assist users with their queries.

## Features:
1. **Answering "How-to" Questions:**
   - The chatbot can respond to questions related to various tasks within the four CDPs (Segment, mParticle, Lytics, and Zeotap).
   - Example questions:
     - "How do I set up a new source in Segment?"
     - "How can I create a user profile in mParticle?"
     - "How do I build an audience segment in Lytics?"
     - "How can I integrate my data with Zeotap?"

2. **Fetching Documentation:**
   - The chatbot fetches official documentation from the respective CDP websites.
   - It uses web scraping techniques (with BeautifulSoup) to retrieve the content of the documentation.

3. **Natural Language Processing (NLP):**
   - The chatbot uses the **NLTK** library to process the text and query input from users, including:
     - Tokenizing, lemmatizing, and removing stop words.
   - The system uses **TF-IDF** vectorization to represent documentation and user queries for efficient matching.

4. **Cosine Similarity for Answer Retrieval:**
   - The chatbot compares the user's question with the documentation using cosine similarity to find the most relevant answers.

5. **Cross-CDP Comparisons:**
   - The chatbot can compare different CDPs based on user queries, such as: "How does Segment’s audience creation process compare to Lytics’?"

6. **Advanced Queries:**
   - The chatbot handles complex "how-to" questions and provides detailed steps, configurations, or integration guidance across multiple platforms.

## Evaluation Criteria:
- **Accuracy of Responses:** Correctness and relevance of the answers provided based on the documentation.
- **Handling of Variations:** Ability to understand and respond to different question phrasings and terminologies.
- **Bonus Features:** Implementation of cross-CDP comparisons and handling more advanced questions.
- **User Experience:** Clarity and usability of the chatbot responses.
- **Code Quality:** Clean, maintainable, and efficient code.

## Technologies Used:
- **Python** for backend development.
- **NLTK** for natural language processing.
- **BeautifulSoup** for web scraping.
- **TF-IDF Vectorization** from `scikit-learn` for document comparison.
- **Cosine Similarity** for matching queries with documentation.
- **Requests** for making HTTP requests to fetch documentation.
