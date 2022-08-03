from django.db import models

# Create your models here.
class Member(models.Model):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()


	def __str__(self):
		return self.first_name + " " + self.last_name


class Know(models.Model):
	title = models.CharField(max_length=250, default='KNOW GOD')
	attend_worship_service = models.BooleanField()
	starting_point = models.BooleanField()
	commit_life_to_christ = models.BooleanField()
	recommit_life_to_christ = models.BooleanField()
	baptism = models.BooleanField()
	join_the_church = models.BooleanField()
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.member)




class Connect(models.Model):
	title = models.CharField(max_length=250, default='CONNECT TO COMMUNITY')
	complete_a_connect_card = models.BooleanField()
	attend_life_group = models.BooleanField()
	attend_community_gathering = models.BooleanField()
	attend_a_mens_or_womens_event = models.BooleanField()
	participate_in_an_Age_Graded_Ministry = models.BooleanField()
	join_our_mailing_list_or_notification_list = models.BooleanField()
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.member)


class Grow(models.Model):
	title = models.CharField(max_length=250, default='GROW SPIRITUALLY')
	read_the_Bible = models.BooleanField()
	engage_in_Gods_word_through_journaling = models.BooleanField()
	memorize_scripture = models.BooleanField()
	join_a_D_group = models.BooleanField()
	lead_a_d_group = models.BooleanField()
	attend_a_mid_week_study = models.BooleanField()
	fast_and_pray = models.BooleanField()
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.member)


class Change(models.Model):
	title = models.CharField(max_length=250, default='CHANGE THE WORLD')
	invite_someone_to_church = models.BooleanField()
	bring_a_guest_to_church = models.BooleanField()
	have_a_gospel_conversation = models.BooleanField()
	join_a_serving_team = models.BooleanField()
	give_for_the_first_time = models.BooleanField()
	become_a_repeat_giver = models.BooleanField()
	become_a_regular_giver = models.BooleanField()
	go_on_a_mission_trip = models.BooleanField()
	lead_a_neighborhood_mission_project = models.BooleanField()
	take_a_spiritual_gifts_inventory = models.BooleanField()
	share_church_content_on_social_media = models.BooleanField()
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.member)




	
