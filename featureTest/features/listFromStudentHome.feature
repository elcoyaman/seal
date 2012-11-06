Feature: As a student I want to see de courses where i am enrolled and the practices of this courses 

 	Scenario: No Course Enrolled
 		Given course "2012-1" exists
 		  And exist student "Martin" without course
 		 When I enter in the "Martin" home page
 		 Then I should see "Courses where are you enrolled"
 
	Scenario: Enrolled in two courses, order by newest course
		Given course "2012-1" exists
		  And course "2011-2" exists
		  And user "Martin" is registered
		  And student "Martin" exists in course "2012-1" and in course "2011-2"
		 When I enter in the "Martin" home page
		 Then I should see "2012-1" before "2011-2" 
 		  
	Scenario: List practices of enrroles course without practice
		Given course "2012-1" exists
		  And user "Martin" is registered
		  And student "Martin" exists in course "2012-1"
		 When I enter in the "Martin" home page
		  And I click in the "2012-1" link
		 Then I should see "There are yet no Practices" 
		 
	Scenario: List practices of enrroles course with 2 practices order by deadline 
		Given course "2012-1" exists
		  And user "Martin" is registered
		  And student "Martin" exists in course "2012-1"
		  And practice "TP 1" exists in course "2012-1" with deadline "2012-12-02"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
		 When I enter in the "Martin" home page
		  And I click in the "2012-1" link
		 Then I should see "TP Intro" before "TP 1"	 
 