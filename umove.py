from __future__ import print_function
import myo as libmyo; libmyo.init()
import time

def main():
    feed = libmyo.device_listener.Feed()
    hub = libmyo.Hub()
    hub.run(1000, feed)

    try:
        myo = feed.wait_for_single_device(2)
        if not myo:
            return

        print("Conectado.")
        
        while hub.running and myo.connected:
            try:
                #print(myo.pose)
                print(myo.gyroscope)
                print(myo.acceleration)
                time.sleep(0.025)
            except RuntimeError:
                print("RuntimeError")
        print("Finalizado.")

    except KeyboardInterrupt:
        print("Interrompido pelo teclado")
    else:
        print("Desconectado.")
    finally:
        print("Desligando...")
        hub.shutdown()

if __name__ == "__main__":
    main()
