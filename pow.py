import hashlib
import time

class ProofOfWork:
    def __init__(self, difficulty):
        """
        Inicializa la clase con un nivel de dificultad especificado.
        
        :param difficulty: Número de ceros iniciales requeridos en el hash.
        """
        self.difficulty = difficulty

    def mine_block(self, block_data):
        """
        Realiza el proceso de minería del bloque buscando el nonce correcto que satisfaga la condición de dificultad.
        
        :param block_data: Datos del bloque que se desean minar.
        :return: Tupla (nonce, hash_result) donde nonce es el valor encontrado y hash_result es el hash del bloque.
        """
        nonce = 0
        start_time = time.time()
        while True:
            hash_result = self.calculate_hash(block_data, nonce)
            if hash_result[:self.difficulty] == '0' * self.difficulty:
                end_time = time.time()
                print(f"Block mined! Nonce: {nonce}, Hash: {hash_result}, Time: {end_time - start_time} seconds")
                return nonce, hash_result
            nonce += 1

    def calculate_hash(self, block_data, nonce):
        """
        Calcula el hash SHA-256 para los datos del bloque concatenados con el nonce.
        
        :param block_data: Datos del bloque.
        :param nonce: Valor nonce.
        :return: Hash SHA-256 resultante en formato hexadecimal.
        """
        value = f"{block_data}{nonce}".encode()
        return hashlib.sha256(value).hexdigest()

    def validate_block(self, block_data, nonce):
        """
        Valida que un bloque minado cumple con los requisitos de dificultad.
        
        :param block_data: Datos del bloque.
        :param nonce: Valor nonce que se usó para minar el bloque.
        :return: True si el bloque es válido, False en caso contrario.
        """
        hash_result = self.calculate_hash(block_data, nonce)
        return hash_result[:self.difficulty] == '0' * self.difficulty

# Ejemplo de uso
if __name__ == "__main__":
    difficulty = 4  # Dificultad (número de ceros iniciales en el hash)
    block_data = "Ejemplo de datos del bloque"

    # Crear una instancia de la clase ProofOfWork con la dificultad especificada
    pow = ProofOfWork(difficulty)
    
    # Minar el bloque con los datos proporcionados
    nonce, hash_result = pow.mine_block(block_data)

    # Validación del bloque minado
    is_valid = pow.validate_block(block_data, nonce)
    print(f"¿El bloque es válido? {'Sí' if is_valid else 'No'}")
