from __future__ import absolute_import, division, print_function, unicode_literals


from google.protobuf import text_format
import can_pb2

def read_protobuf_data(filename):
  """Reads and parses the specified ASCII Pb

  Args:
    filename: a string representing the filename to read

  Returns:
    a list of Pb values
  """
  can_messages = can_pb2.CanSchema()
  try:
    with open(filename, 'r') as asciipb:
      text_format.Merge(asciipb.read(), can_messages)
  except Exception as excep:
    raise Exception('Could not parse ASCII Protobuf file %s: %s' %
                    (filename, excep))
  return can_messages.msg

if __name__ == '__main__':
  print(read_protobuf_data('messages.asciipb'))
