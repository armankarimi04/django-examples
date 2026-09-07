from django.core.management.base import BaseCommand
from main.models import Film


class Command(BaseCommand):
    help = 'Create sample films for testing'

    def handle(self, *args, **options):
        films_data = [
            {
                'title': 'The Dark Knight',
                'director': 'Christopher Nolan',
                'release_year': 2008,
                'genre': 'action',
                'rating': 9.0,
                'synopsis': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'duration_minutes': 152,
            },
            {
                'title': 'Pulp Fiction',
                'director': 'Quentin Tarantino',
                'release_year': 1994,
                'genre': 'thriller',
                'rating': 8.9,
                'synopsis': 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.',
                'duration_minutes': 154,
            },
            {
                'title': 'The Shawshank Redemption',
                'director': 'Frank Darabont',
                'release_year': 1994,
                'genre': 'drama',
                'rating': 9.3,
                'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'duration_minutes': 142,
            },
            {
                'title': 'Inception',
                'director': 'Christopher Nolan',
                'release_year': 2010,
                'genre': 'sci-fi',
                'rating': 8.8,
                'synopsis': 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'duration_minutes': 148,
            },
            {
                'title': 'The Godfather',
                'director': 'Francis Ford Coppola',
                'release_year': 1972,
                'genre': 'drama',
                'rating': 9.2,
                'synopsis': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'duration_minutes': 175,
            },
            {
                'title': 'Goodfellas',
                'director': 'Martin Scorsese',
                'release_year': 1990,
                'genre': 'thriller',
                'rating': 8.7,
                'synopsis': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners.',
                'duration_minutes': 146,
            },
            {
                'title': 'The Matrix',
                'director': 'The Wachowskis',
                'release_year': 1999,
                'genre': 'sci-fi',
                'rating': 8.7,
                'synopsis': 'A computer programmer is led to fight an underground war against powerful computers who have constructed his entire reality with a system called the Matrix.',
                'duration_minutes': 136,
            },
            {
                'title': 'Forrest Gump',
                'director': 'Robert Zemeckis',
                'release_year': 1994,
                'genre': 'drama',
                'rating': 8.8,
                'synopsis': 'The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
                'duration_minutes': 142,
            },
            {
                'title': 'The Silence of the Lambs',
                'director': 'Jonathan Demme',
                'release_year': 1991,
                'genre': 'thriller',
                'rating': 8.6,
                'synopsis': 'A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.',
                'duration_minutes': 118,
            },
            {
                'title': 'Spirited Away',
                'director': 'Hayao Miyazaki',
                'release_year': 2001,
                'genre': 'animation',
                'rating': 9.0,
                'synopsis': 'During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits.',
                'duration_minutes': 125,
            },
            {
                'title': 'Parasite',
                'director': 'Bong Joon-ho',
                'release_year': 2019,
                'genre': 'thriller',
                'rating': 8.5,
                'synopsis': 'A poor family schemes to become employed by a wealthy family by infiltrating their household and posing as unrelated, highly qualified individuals.',
                'duration_minutes': 132,
            },
            {
                'title': 'Get Out',
                'director': 'Jordan Peele',
                'release_year': 2017,
                'genre': 'horror',
                'rating': 7.7,
                'synopsis': 'A young African-American visits his white girlfriend\'s parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.',
                'duration_minutes': 104,
            },
            {
                'title': 'Mad Max: Fury Road',
                'director': 'George Miller',
                'release_year': 2015,
                'genre': 'action',
                'rating': 8.1,
                'synopsis': 'In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners.',
                'duration_minutes': 120,
            },
            {
                'title': 'The Grand Budapest Hotel',
                'director': 'Wes Anderson',
                'release_year': 2014,
                'genre': 'comedy',
                'rating': 8.1,
                'synopsis': 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel\'s glorious years.',
                'duration_minutes': 99,
            },
            {
                'title': 'Blade Runner 2049',
                'director': 'Denis Villeneuve',
                'release_year': 2017,
                'genre': 'sci-fi',
                'rating': 8.0,
                'synopsis': 'A young blade runner\'s discovery of a long-buried secret leads him to track down former blade runner Rick Deckard.',
                'duration_minutes': 164,
            },
        ]

        created_count = 0
        for film_data in films_data:
            film, created = Film.objects.get_or_create(
                title=film_data['title'],
                release_year=film_data['release_year'],
                defaults=film_data
            )
            
            if created:
                created_count += 1
                print(f'Created film: {film.title} ({film.release_year})')
            else:
                print(f'Film already exists: {film.title} ({film.release_year})')

        print(f'\nSuccessfully created {created_count} films!')