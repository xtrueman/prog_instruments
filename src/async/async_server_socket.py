#!python3

import asyncio

async def handle_client(reader, writer):
    try:
        while True:  # Бесконечный цикл для чтения данных от клиента
            data = await reader.read(100)  # Чтение данных (максимум 100 байт)
            if not data:
                break  # Если данных нет, закрыть соединение
            read_len = len(data)
            response = f"Len: {read_len}\n".encode('utf-8')
            writer.write(response)
            await writer.drain()  # Гарантируем отправку данных
    except asyncio.CancelledError:
        # Соединение может быть отменено при закрытии сервера
        writer.close()
        await writer.wait_closed()
    finally:
        writer.close()  # Убедимся, что соединение закрывается корректно
        await writer.wait_closed()

async def main(host='127.0.0.1', port=5001):
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()  # Сервер будет работать бесконечно

asyncio.run(main())
