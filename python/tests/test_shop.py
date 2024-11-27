from shop import Shop, User


def test_happy_path(fsf_address):
    user = User.Builder().with_age(25).with_verified(True).with_address(fsf_address).build()
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=25,
    #     address=fsf_address,
    #     verified=True,
    # )

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = User.Builder().with_age(16).build()
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=16,
    #     address=fsf_address,
    #     verified=True,
    # )

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    user = User.Builder().with_age(19).with_verified(False).build()
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=16, #FIXME: faut pas tester pour mineur faut tester que pour not verified
    #     address=fsf_address,
    #     verified=False,
    # )

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(paris_address):
    user = User.Builder().with_address(paris_address).build()
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=25,
    #     address=paris_address,
    #     verified=False,
    # )

    assert Shop.must_pay_foreign_fee(user)
