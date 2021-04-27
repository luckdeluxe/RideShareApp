# RideShareApp
It is a private carpooling platform that was born with the need to cover transportation costs for students and private organizations in the city of Buenos Aires.
## About
The platform is private with users and groups. A user can join the platform only with an invitation code. Users can invite other users, these invitations are limited.
Groups can be public or private (organizations). Within the groups, users can offer or join a trip. The trips are limited to people.
At the end of each trip, users rate the experience. Each user has a general reputation and is public for the rest of the users.
## Development
To start working on this project I highly recommend you to check
[pydanny's](https://github.com/pydanny) [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django) [documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html) on how to get this project up and running locally.
If you don't want to do so, just run:

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up
```

## Contributing

I'll be happily accepting pull requests from anyone.
This that are missing right now:

* [ ] Add tests and coverage implementations
* [ ] Remove weak Token Authorization system
* [ ] Implement more async and periodic tasks to improve the rating system
* [ ] A UI!

Suggestions are welcome!

## Want to use this project as yours?

Please stick to the [**LICENSE**](LICENSE), you can read a TL;DR
[here](https://tldrlegal.com/license/mit-license).

Again, this is a project I liked a lot and I will love to see it live
again. Feel free to modify, distribute, use privately, etc (READ THE [**LICENSE**](LICENSE)) as
you please just include the Copyright and the [**LICENSE**](LICENSE).
