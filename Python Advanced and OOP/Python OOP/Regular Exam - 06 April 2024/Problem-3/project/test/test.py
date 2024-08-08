from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia('Space', 'YouTube', 100, 'news')

    def test_social_media_structure(self):
        self.assertTrue(hasattr(SocialMedia, "_validate_and_set_platform"))
        self.assertTrue(hasattr(SocialMedia, "create_post"))
        self.assertTrue(hasattr(SocialMedia, "like_post"))
        self.assertTrue(hasattr(SocialMedia, "comment_on_post"))

        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))

    def test_constructor(self):
        self.assertIsInstance(self.social_media, SocialMedia)
        self.assertEqual(self.social_media._username, 'Space')
        self.assertEqual(self.social_media._platform, 'YouTube')
        self.assertEqual(self.social_media._followers, 100)
        self.assertEqual(self.social_media._content_type, 'news')
        self.assertEqual(self.social_media._posts, [])

    def test_platform_validation_with_valid_platform(self):
        self.social_media._platform = 'Instagram'
        self.assertEqual(self.social_media._platform, 'Instagram')

        self.social_media._platform = 'Twitter'
        self.assertEqual(self.social_media._platform, 'Twitter')

        self.social_media._validate_and_set_platform('Instagram')
        self.assertEqual(self.social_media._platform, 'Instagram')

    def test_platform_validation_with_not_valid_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media._validate_and_set_platform('twitter')
        self.assertEqual(str(ve.exception), f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

        with self.assertRaises(ValueError) as ve:
            self.social_media._validate_and_set_platform('asd')
        self.assertEqual(str(ve.exception), f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_followers_validation_with_valid_followers_that_are_positive_integers(self):
        self.social_media.followers = 100
        expect = 100
        actual = self.social_media.followers
        self.assertEqual(expect, actual)

        self.social_media.followers = 0
        expect = 0
        actual = self.social_media.followers
        self.assertEqual(expect, actual)

    def test_followers_validation_with_invalid_followers_that_are_below_zero(self):
        invalid_followers = -1
        with self.assertRaises(ValueError) as context:
            self.social_media.followers = invalid_followers
        self.assertEqual(str(context.exception), "Followers cannot be negative.")

    def test_create_post(self):
        self.assertEqual(len(self.social_media._posts), 0)

        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        self.assertEqual(len(self.social_media._posts), 1)

        expected_post = {
            'content': post_content,
            'likes': 0,
            'comments': []
        }
        self.assertEqual(self.social_media._posts[0], expected_post)

        expected_message = 'New news post created by Space on YouTube.'
        actual_message = self.social_media.create_post(post_content)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_with_valid_increment_likes__success(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        initial_likes = self.social_media._posts[0]['likes']
        self.assertEqual(initial_likes, 0)

        self.social_media.like_post(0)

        self.assertEqual(self.social_media._posts[0]['likes'], initial_likes + 1)

        expected_message = f"Post liked by Space."
        actual_message = self.social_media.like_post(0)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_reach_max_likes__expect_to_return_correct_message(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)
        self.social_media._posts[0]['likes'] = 9

        initial_likes = self.social_media._posts[0]['likes']
        self.assertEqual(initial_likes, 9)

        self.social_media.like_post(0)

        self.assertEqual(self.social_media._posts[0]['likes'], 10)

        expected_message = "Post has reached the maximum number of likes."
        actual_message = self.social_media.like_post(0)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_case_with_invalid_index(self):
        result = self.social_media.like_post(-20)
        self.assertEqual(result, 'Invalid post index.')

        self.social_media._posts = [{'likes': 0}, {'likes': 10}, {'likes': 200}]
        result = self.social_media.like_post(3)
        self.assertEqual(result, 'Invalid post index.')

        self.social_media._posts = [{'likes': 0}]
        result = self.social_media.like_post(-1)
        self.assertEqual(result, 'Invalid post index.')

    def test_valid_comment_on_post_case(self):
        self.social_media._posts = [{'comments': [], 'content': 'Movies', 'likes': 0}]
        result = self.social_media.comment_on_post(0, 'This is awesome!')
        self.assertEqual(result, 'Comment added by Space on the post.')

    def test_invalid_comment_on_post_case(self):
        self.social_media._posts = [{'comments': [], 'content': 'Movies', 'likes': 0}]
        result = self.social_media.comment_on_post(0, 'awesome!')
        self.assertEqual(result, 'Comment should be more than 10 characters.')


if __name__ == '__main__':
    main()
