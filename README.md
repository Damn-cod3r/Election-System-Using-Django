# Election System App

## Overview
The **Election System App** is a simple and efficient voting platform designed to allow users to cast votes and view results in real-time. The app provides a straightforward interface where users can select a candidate and submit their vote. It also displays the total number of votes for each candidate.

## Features
- **Voting Interface**: Users can cast their vote for one of the available candidates.
- **Real-time Results**: After voting, users can view the total number of votes each candidate has received.
- **No Login Required**: The app currently does not require users to log in to cast a vote or view results, making the process quick and accessible.

## Screenshots

### Voting Screen
![Voting Screen](path_to_your_screenshot_voting.png)

The voting screen displays a list of candidates (Person 1, Person 2, Person 3, Person 4). Users can select one candidate and submit their vote via the `Submit` button.  
URL: `http://127.0.0.1:8000/election/vote/`

### Results Screen
![Results Screen](path_to_your_screenshot_results.png)

After voting, users are directed to the results screen, which shows the total votes for each candidate.  
URL: `http://127.0.0.1:8000/election/results/`

## Example Results:
- Person 1: 20 votes
- Person 2: 30 votes
- Person 3: 5 votes
- Person 4: 7 votes

## Installation & Setup
1. Clone the repository or download the project files.
2. Ensure Python and Django are installed in your environment.
3. Run the following command to start the Django server:
    ```bash
    python manage.py runserver
    ```
4. Access the app by navigating to `http://127.0.0.1:8000/election/vote/` for voting and `http://127.0.0.1:8000/election/results/` for results.

## Future Enhancements
- **User Authentication**: Implement a login system to ensure that each user can vote only once.
- **Improved User Interface**: Enhance the visual design of the app for a more user-friendly experience.
- **Multiple Elections Support**: Add functionality to handle multiple elections and different voting types.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any issues or contributions, please contact chidambaram sekar at chidambaram097@gmail.com.
