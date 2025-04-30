import pytest


@pytest.mark.parametrize(
    "first_name, last_name, number_phone, about_me, status_code",
    [
        ("kirill", "Belskiy", "+79031602381", "test-opsanie", 200),
        ("", "", "", "", 200),
        ("", "", 2, 22, 422),
    ],
)
async def test_add_and_get_bookings(
    first_name, last_name, number_phone, about_me, status_code, authenticated_ac
):
    res = await authenticated_ac.patch(
        "/users/edit",
        json={
            "first_name": first_name,
            "last_name": last_name,
            "number_phone": number_phone,
            "about_me": about_me,
        },
    )
    assert res.status_code == status_code

    response = await authenticated_ac.get(
        "/users/me",
    )

    assert response.status_code == 200
