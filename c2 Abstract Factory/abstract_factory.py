from abc import ABC, abstractmethod


class AbstractApiLondrina(ABC):
    def __init__(self, token):
        self.token = token

        @abstractmethod
        def collect_data(self):
            pass


class ApiLondrinaTransport(AbstractApiLondrina):
    def collect_data(self):
        return f"Dados coletados ApiLondrinaTransport por meio do token: {self.token}"


class ApiLondrinaSecurity(AbstractApiLondrina):
    def collect_data(self):
        return f"Dados coletados ApiLondrinaSecurity por meio do token: {self.token}"


class AbstractApiParana(ABC):
    def __init__(self, token):
        self.token = token

        @abstractmethod
        def collect_data(self):
            pass

        @abstractmethod
        def collect_data_by_city(self, city):
            pass


class ApiParanaTransport(AbstractApiParana):
    def collect_data(self):
        return f"Dados coletados ApiParanaTransport por meio do token: {self.token}"

    def collect_data_by_city(self, city):
        return f"Dados coletados da cidade {city}, ApiParanaTransport por meio do token: {self.token}"


class ApiParanaSecurity(AbstractApiParana):
    def collect_data(self):
        return f"Dados coletados ApiParanaSecurity por meio do token: {self.token}"

    def collect_data_by_city(self, city):
        return f"Dados coletados da cidade {city}, ApiParanaSecurity por meio do token: {self.token}"


class AbstractApiFactory(ABC):
    def __init__(self, token_londrina, token_parana):
        self.token_londrina = token_londrina
        self.token_parana = token_parana

    @abstractmethod
    def create_api_londrina(self):
        pass

    @abstractmethod
    def create_api_parana(self):
        pass


class TransportDataFactory(AbstractApiFactory):
    def create_api_londrina(self):
        return ApiLondrinaTransport(self.token_londrina)

    def create_api_parana(self):
        return ApiParanaTransport(self.token_parana)


class SecurityDataFactory(AbstractApiFactory):
    def create_api_londrina(self):
        return ApiLondrinaSecurity(self.token_londrina)

    def create_api_parana(self):
        return ApiParanaSecurity(self.token_parana)


def cliente_code(factory: AbstractApiFactory):
    product_londrina = factory.create_api_londrina()
    product_parana = factory.create_api_parana()

    print(product_londrina.collect_data())
    print(product_parana.collect_data_by_city("Maringa"))


if __name__ == "__main__":
    token_londrina = "user_londrina_123"
    token_parana = "user_parana_321"

    print("Coletando dados de transporte...")
    cliente_code(TransportDataFactory(token_londrina, token_parana))

    print("Coletando dados de segurança...")
    cliente_code(SecurityDataFactory(token_londrina, token_parana))
