import "github.com/hashicorp/vault/shamir"

const (
    // ShareOverhead is the byte size overhead of each share
    // when using Split on a secret. This is caused by appending
    // a one byte tag to the share.
    ShareOverhead = 1
)

func Split(secret []byte, parts, threshold int) ([][]byte, error)
