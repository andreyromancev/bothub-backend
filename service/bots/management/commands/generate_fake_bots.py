import random
from django.core.management.base import BaseCommand
from ...models import BotProfile


class Command(BaseCommand):
    NAME_WORDS = ('bot', 'test', 'this', 'awesome', 'name', 'bobook', 'super', 'random')
    DESCRIPTION_WORDS = ('bot', 'test', 'this', 'awesome', 'description', 'long', 'text', 'random')

    def add_arguments(self, parser):
        parser.add_argument('bots_count', type=int)

        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear',
            default=False,
            help='Delete all existing bots before generation',
        )

    def handle(self, *args, **options):
        if options['clear']:
            BotProfile.objects.all().delete()

        if BotProfile.objects.exists():
            start_user_id = BotProfile.objects.last().id + 1
        else:
            start_user_id = 0

        for i in range(start_user_id, start_user_id + options['bots_count']):
            BotProfile.objects.create(
                user_id=i,
                name='{}. {}'.format(i, self._get_name()),
                short_description=self._get_short_description()
            )

        self.stdout.write(self.style.SUCCESS('Bots generated!'))

    def _get_name(self):
        random.seed()
        words_count = random.randint(1, 3)
        words = tuple(random.choice(self.NAME_WORDS) for i in range(0, words_count))

        return '_'.join(words)

    def _get_short_description(self):
        random.seed()
        words_count = random.randint(10, 25)
        words = tuple(random.choice(self.DESCRIPTION_WORDS) for i in range(0, words_count))

        return ' '.join(words)
